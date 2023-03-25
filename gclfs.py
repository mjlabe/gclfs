import click
from command.command import pass_command
from storage.upload import cloud_upload


@click.command()
@click.option('-s',
              is_flag=True,
              show_default=True,
              default=True,
              help="AWS S3 Storage")
@click.argument('command')
@click.argument('param', required=False)
def gclfs(s, command, param=None):
    cloud_paths = cloud_upload(s)
    with open(".paths", "w+") as paths_file:
        print(paths_file.read())
    pass_command(command, param)
