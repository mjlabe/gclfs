import os

import click

from gclfs.commands import handle_command
from storage.upload import cloud_upload


@click.command(name='ctx', context_settings=dict(
    ignore_unknown_options=True,
    allow_extra_args=True,
))
@click.option('-s',
              is_flag=True,
              show_default=True,
              default=True,
              help="AWS S3 Storage")
@click.pass_context
def cli(ctx, s):
    handle_command(ctx.args, s)
