import os
from storage.upload import cloud_upload


def handle_command(ctx, s):
    print(ctx, s)
    command = ""
    for cmd in ctx:
        command += f"{cmd} "
    print(command)
    os.system(f"git {command}")
    if command == "commit":
        cloud_upload(s)
