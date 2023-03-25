import os


def pass_command(command, param=None):
    print(command, param)
    if param:
        os.system(f"git {command} {param}")
    else:
        os.system(f"git {command}")
