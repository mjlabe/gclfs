import os

from storage.sync import CloudSync


def handle_command(args, s):
    print(args, s)
    command = ""
    for cmd in args:
        command += f"{cmd} "
    print(command)
    # show sync status (extra/missing files)

    if command.startswith("push"):
        cs = CloudSync(s)
        cs.cloud_sync()

    os.system(f"git {command}")


def track(args):
    attr_file = open(".gitattributes", "a+")
    attr_file.seek(0)
    attrs = attr_file.readlines()
    for line in attrs:
        if line.startswith(args[1]):
            print(f'"{args[1]}" already supported')
            return
    attr_file.write(f"{args[1]} filter=gclfs diff=gclfs merge=gclfs -text\n")
