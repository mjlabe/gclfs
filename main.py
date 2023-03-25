import click

from gclfs.commands import handle_command, track


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
    commands = {
        "track": track,
    }
    if ctx.args[0] in commands:
        commands.get(ctx.args[0])(ctx.args)
    else:
        handle_command(ctx.args, s)
