import os
from pathlib import Path

from storage.sync import CloudSync


def parse_git_command(args, s=None):
    print(args, s)
    command = " ".join(args)
    print(command)
    return command


def track(args, s=None):
    with open(".gitattributes", "a+") as attr_file:
        attr_file.seek(0)
        attrs = attr_file.readlines()
        for line in attrs:
            if line.startswith(args[1]):
                print(f'"{args[1]}" already supported')
                return
        attr_file.write(f"{args[1]} filter=gclfs diff=gclfs merge=gclfs -text\n")


def sync(s, project_root):
    print(f"Syncing files with {s}")
    cs = CloudSync(s, project_root)
    cs.cloud_sync()


def clone(args, s):
    command = parse_git_command(args)
    os.system(f"git {command}")
    project_root = command.split(" ")[-1].split("/")[-1].split(".")[0]
    sync(s, Path(os.getcwd(), project_root))


def push(args, s):
    os.system(f"git {parse_git_command(args)}")
    sync(s, os.getcwd())


def pull(args, s):
    os.system(f"git {parse_git_command(args)}")
    sync(s, os.getcwd())


def default(args):
    parse_git_command(args)
