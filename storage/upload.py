def cloud_upload(s):
    with open(".paths", "w+") as paths_file:
        print(paths_file.read())
    print(s)
