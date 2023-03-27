import click

from src.gclfs.commands.commands import default, track, clone, push, pull


@click.command(name='ctx', context_settings=dict(
    ignore_unknown_options=True,
    allow_extra_args=True,
))
@click.option('--storage', default="s3", show_default=True)
@click.pass_context
def cli(ctx, storage):
    commands = {
        "clone": clone,
        "push": push,
        "pull": pull,
    }
    try:
        if ctx.args[0] == "track":
            track(ctx.args)
        elif ctx.args[0] in commands:
            commands.get(ctx.args[0])(ctx.args, storage)
        else:
            default(ctx.args)
    except Exception as error:
        print(f'ERROR: Command "{" ".join(ctx.args)}" not recognized. {error}')
