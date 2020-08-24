from .. import regions

import click
from . import cli


@cli.command()
@click.option(
    "--bedfiles",
    # multiple=True,
    type=str,
   # default=[],

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
    type=str,
    #multiple=True,
    #default=['test.bed']

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
# @click.argument('out', 
#                 type=click.File('w'), 
#                 default='-', 
#                 required=False)

def compute_regions(bigwig, bedfiles, plot):
    """Get mean value for regions from bigwig."""
    bedfiles_split = bedfiles.split(',')
    bigwig_split = bigwig.split(',')

    stack = regions.regions_mean(bigwig_split, bedfiles_split)
    print(stack)
    plotarray = regions.create_plotarray2(stack,bigwig_split)
    print(plotarray)
    if plot != None:
        print('Entered plot method')
        regions.plot(ndarray=plotarray, col_names=bedfiles_split, row_names=bigwig_split, output=plot)
    return plotarray 