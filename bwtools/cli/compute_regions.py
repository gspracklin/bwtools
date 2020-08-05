from .. import regions

import click
from . import cli


@cli.command()
@click.option(
    "--bedfiles",
    help="List of bed files. ['regions1.bed','regions2.bed', ...]",
    nargs=3,
    default=[],
    required=True,
)
# @click.option(
#     "-v", "--verbose",
#     help="Enable verbose output",
#     is_flag=True,
#     default=False
# )
@click.option(
    "--bigwig", "-bw",
    help="List of bigwig files. ['test1.bw','test2.bw', ...]",
    default=[],
    required=True,
)
@click.option(
    "--array", "-a", 
    help="List of raw values per domains.",
    type=str,
    required=True,
)
@click.option(
    "--plot",  
    help="plot filename",
    type=str,
    required=True,
)
@click.argument('out', 
                type=click.File('w'), 
                default='-', 
                required=False)

def compute_regions(bigwig, bedfiles, plot=True,array=True):
    """Get mean value for regions from bigwig."""
    print('the bedfiles are ', bedfiles)
    print('the bigwigs are ', bigwig)
    for i in bigwig:
        print(i)
    stack = regions.regions_mean(bigwig, bedfiles)
    plotarray = regions.create_plotarray(stack, bigwig, bedfiles, file=out)
    if plot == True:
        plot(plotarray, bigwig, bedfiles, output=plot)
    return plotarray