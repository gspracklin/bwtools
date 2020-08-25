from .. import regions

import click
from . import cli


@cli.command()
@click.option(
    "--bedfiles",
    type=str,
)
@click.option(
    "--bigwigs",
    help="List of bigwig files (comma sep).",
    type=str,
)
# @click.option(
#     "--array", "-a", 
#     help="List of raw values per domains.",
#     type=str,
# )
@click.option(
    "--plot",  
    help="plot filename",
    type=str,
    default=None
)

def compute_regions(bigwigs, bedfiles, plot):
    """Get mean value for regions from bigwig."""
    bedfiles_split = bedfiles.split(',')
    bigwigs_split = bigwigs.split(',')

    stack = regions.regionsTwolists(bigwig_split, bedfiles_split)
    plotarray = regions.create_plotarray(stack,bigwig_split)
 
    if plot != None:
        regions.plot(plotarray, col_names=bedfiles_split, row_names=bigwig_split, output=plot)
    return plotarray 