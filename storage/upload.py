import json
import os


def cloud_upload(s):
    """
    Iterate through files in `.gclfsattributes` and upload if checksum has changed
    :param s:
    :return:
    """
    print("upload", s)
    if not os.path.exists("file.txt"):
        attr_file = open(".gclfsattributes", "w+")
    else:
        attr_file = open(".gclfsattributes", "a+")
    attrs = json.load(attr_file)
    # for file in .gclfsattribues
    # if hash has changed, upload
