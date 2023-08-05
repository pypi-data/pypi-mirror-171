"""
To work the volumes folder must be a child of a zfs filesystem:
zfs create zfs_pool1/docker
zfs create zfs_pool1/docker/volumes

set /etc/odoo/settings ZFS_PATH_VOLUMES=zfs_pool1/docker/volumes  then

"""
from .tools import abort
from operator import itemgetter
import subprocess
import arrow
import sys
import shutil
import tempfile
import click
from .tools import __dc
from .tools import search_env_path
from . import cli, pass_config
from .lib_clickhelpers import AliasedGroup
from pathlib import Path
from .tools import abort

HOWTO_PREPARE = """

Preperation docker - be careful - make backups

systemctl stop docker
mv /var/lib/docker /var/lib/docker.old
mkdir -p /var/lib/docker/volumes
zfs create -p rpool/.../var/lib/docker/volumes
rsync /var/lib/docker.old/ /var/lib/docker/ -arP
rm -Rf /var/lib/docker.old
systemctl start docker

"""

DOCKER_VOLUMES = Path("/var/lib/docker/volumes")


class NotZFS(Exception):
    def __init__(self, msg, poolname):
        super().__init__(msg)
        self.poolname = poolname


def unify(text):
    while "\t" in text:
        text = text.replace("\t", " ")
    while "  " in text:
        text = text.replace("  ", " ")
    return text


def _get_path(config):
    path = DOCKER_VOLUMES / __get_postgres_volume_name(config)
    return path


def _get_zfs_path(config):
    if not config.ZFS_PATH_VOLUMES:
        abort(
            "Please configure the snapshot root folder for docker "
            "snapshots in ZFS_PATH_VOLUMES"
        )
    path = config.ZFS_PATH_VOLUMES + "/" + __get_postgres_volume_name(config)
    return path


def _get_next_snapshotpath(config):
    counter = 0
    while True:
        path = _get_zfs_path(config)
        path = str(path) + f".{counter}"
        if not __is_zfs_fs(path):
            break
        counter += 1
    return path


def _get_possible_snapshot_paths(config):
    """
    :param path: root path
    """
    all_zfs_folders = _get_all_zfs()
    zfs_path = _get_zfs_path(config)
    root_zfs_path = "/".join(zfs_path.split("/")[:-1])
    for folder in all_zfs_folders:
        if folder == zfs_path:
            yield folder
        if folder.startswith(zfs_path + "."):
            yield folder


def __get_postgres_volume_name(config):
    return f"{config.project_name}_odoo_postgres_volume"


def __get_snapshots(config):
    path = _get_path(config)
    try:
        return _get_snapshots(config)
    except NotZFS:
        abort(f"Path {path} is not a zfs.")


def _get_snapshots(config):
    zfs = search_env_path("zfs")

    def _get_snaps():
        for path in _get_possible_snapshot_paths(config):
            for line in (
                subprocess.check_output(
                    ["sudo", zfs, "list", "-t", "snapshot", str(path)],
                    encoding="utf8",
                    stderr=subprocess.DEVNULL,  # ignore output of 'no datasets available'
                )
                .strip()
                .splitlines()[1:]
            ):
                snapshotname = unify(line.split(" "))[0]
                creation = unify(
                    subprocess.check_output(
                        ["sudo", zfs, "get", "-p", "creation", snapshotname],
                        encoding="utf8",
                    )
                    .strip()
                    .splitlines()[1]
                )
                _, _, timestamp, _ = creation.split(" ")
                timestamp = arrow.get(int(timestamp)).datetime
                info = {}
                info["date"] = timestamp
                info["fullpath"] = snapshotname
                info["name"] = snapshotname.split("@")[1]
                info["path"] = snapshotname.split("/")[-1]
                yield info

    yield from sorted(_get_snaps(), key=lambda x: x["date"], reverse=True)


def _get_all_zfs():
    zfs = search_env_path("zfs")
    folders = subprocess.check_output(
        ["sudo", zfs, "list"], encoding="utf8"
    ).splitlines()
    folders = list(map(lambda x: x.split(" ")[0], folders))
    return folders


def __is_zfs_fs(path_zfs):
    assert " " not in path_zfs
    folders = _get_all_zfs()
    folders = [x for x in folders if x.split(" ")[0] == path_zfs]
    return folders


def assert_environment(config):
    pass


def _turn_into_subvolume(config):
    """
    Makes a zfs pool out of a path.
    """
    zfs = search_env_path("zfs")
    fullpath = _get_path(config)
    fullpath_zfs = _get_zfs_path(config)
    if __is_zfs_fs(fullpath_zfs):
        # is zfs - do nothing
        return

    filename = fullpath.parent / Path(tempfile.mktemp()).name
    if filename.exists():
        raise Exception(f"Path {filename} should not exist.")
    shutil.move(fullpath, filename)
    try:
        subprocess.check_output(["sudo", zfs, "create", fullpath_zfs])
        click.secho(
            f"Writing back the files to original position: from {filename}/ to {fullpath}/"
        )
        subprocess.check_call(
            [
                "sudo",
                "rsync",
                str(filename) + "/",
                str(fullpath) + "/",
                "-ar",
            ]
        )
    finally:
        subprocess.check_call(["sudo", "rm", "-Rf", filename])


def make_snapshot(ctx, config, name):
    zfs = search_env_path("zfs")
    __dc(["stop", "-t 1"] + ["postgres"])
    path = _get_path(config)
    _turn_into_subvolume(config)
    snapshots = list(_get_snapshots(config))
    snapshot = list(filter(lambda x: x["name"] == name, snapshots))
    if snapshot:
        if config.force:
            subprocess.check_call(["sudo", zfs, "destroy", snapshot[0]["fullpath"]])
        else:
            click.secho(f"Snapshot {name} already exists.", fg="red")
            sys.exit(-1)

    assert " " not in name
    fullpath = _get_zfs_path(config) + "@" + name
    subprocess.check_call(["sudo", zfs, "snapshot", fullpath])
    __dc(["up", "-d"] + ["postgres"])
    return name


def restore(config, name):
    zfs = search_env_path("zfs")
    umount = search_env_path("umount")
    if not name:
        return

    assert "@" not in name
    assert "/" not in name

    snapshots = list(_get_snapshots(config))
    snapshot = list(filter(lambda x: x["name"] == name, snapshots))
    if not snapshot:
        abort(f"Snapshot {name} does not exist.")
    snapshot = snapshot[0]
    zfs_full_path = _get_zfs_path(config)
    snapshots_of_volume = [
        x for x in snapshots if x["fullpath"].split("@")[0].startswith(zfs_full_path)
    ]
    try:
        index = list(map(lambda x: x["name"], snapshots_of_volume)).index(name)
    except ValueError:
        index = -1

    __dc(["stop", "-t 1"] + ["postgres"])
    if index == 0:
        # restore last one is easy in the volumefolder it self; happiest case
        subprocess.check_call(["sudo", zfs, "rollback", snapshot["fullpath"]])
    else:
        full_next_path = _get_next_snapshotpath(config)
        subprocess.check_call(
            ["sudo", umount, zfs_full_path],
        )
        subprocess.check_call(["sudo", zfs, "rename", zfs_full_path, full_next_path])
        subprocess.check_call(
            [
                "sudo",
                zfs,
                "clone",
                full_next_path + "@" + snapshot["name"],
                zfs_full_path,
            ]
        )
    __dc(["rm", "-f"] + ["postgres"])
    __dc(["up", "-d"] + ["postgres"])


def remove(config, snapshot):
    zfs = search_env_path("zfs")
    snapshots = __get_snapshots(config)
    if isinstance(snapshot, str):
        snapshots = [x for x in snapshots if x["name"] == snapshot]
        if not snapshots:
            click.secho(f"Snapshot {snapshot} not found!", fg="red")
            sys.exit(-1)
        snapshot = snapshots[0]
    if snapshot["fullpath"] in map(itemgetter("fullpath"), snapshots):
        subprocess.check_call(["sudo", zfs, "destroy", "-R", snapshot["fullpath"]])


def remove_volume(config):
    zfs = search_env_path("zfs")
    umount = search_env_path("umount")
    for path in _get_possible_snapshot_paths(config):
        subprocess.check_call(["sudo", zfs, "set", "canmount=noauto", path])
        try:
            subprocess.check_call(["sudo", umount, path])
        except:
            pass
        subprocess.check_call(["sudo", zfs, "destroy", "-R", path])
        click.secho(f"Removed: {path}", fg="yellow")
