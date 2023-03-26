import os
from pathlib import Path

from storage.sync import CloudSync


def parse_git_command(args):
    command = " ".join(args)
    print(command)
    return command


def track(args):
    with open(".gitattributes", "a+") as attr_file:
        attr_file.seek(0)
        attrs = attr_file.readlines()
        for line in attrs:
            if line.startswith(args[1]):
                print(f'"{args[1]}" already supported')
                return
        attr_file.write(f"{args[1]} filter=gclfs diff=gclfs merge=gclfs -text\n")


def sync(project_root, storage, method):
    print(f"Syncing files with {storage}")
    cs = CloudSync(project_root, storage)
    cs.cloud_sync(project_root, method)


def clone(args, storage):
    command = parse_git_command(args)
    os.system(f"git {command}")
    project_root = command.split(" ")[-1].split("/")[-1].split(".")[0]
    sync(Path(os.getcwd(), project_root), storage, "pull")


def push(args, storage):
    os.system(f"git {parse_git_command(args)}")
    sync(os.getcwd(), storage, "push")


def pull(args, storage):
    os.system(f"git {parse_git_command(args)}")
    sync(os.getcwd(), storage, "pull")


def default(args):
    parse_git_command(args)
