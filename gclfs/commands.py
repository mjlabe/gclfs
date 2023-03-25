import os
import hashlib

from storage.upload import cloud_upload


def gclfs_add():
    if not os.path.exists("file.txt"):
        attr_file = open(".gclfsattributes", "w+")
    else:
        attr_file = open(".gclfsattributes", "a+")
    attr_file_lines = attr_file.readlines()
    gclfs_file_types = [attr_file_line.split(" ")[0].replace("*", "") for attr_file_line in attr_file_lines]
    # get list of files with that file type
    print(gclfs_file_types)
    for subdir, dirs, files in os.walk("../"):
        for file in files:
            print(os.path.join(subdir, file))
            if file.split(".")[-1] in gclfs_file_types:
                with open(file) as glfs_file:
                    hashlib.md5(glfs_file)
                    # check hash diff
                    # if diff, update .glfsattributes


def handle_command(args, s):
    print(args, s)
    command = ""
    for cmd in args:
        command += f"{cmd} "
    print(command)

    if command.startswith("add"):
        gclfs_add()

    if command.startswith("push"):
        cloud_upload(s)

    os.system(f"git {command}")
