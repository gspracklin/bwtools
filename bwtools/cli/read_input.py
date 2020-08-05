from .. import hmm
import click
from . import cli

@cli.command()
@click.argument('files', nargs=-1, type=click.Path())
def read_input(files):
    """Print all FILES file names."""
    for filename in files:
        click.echo(filename)