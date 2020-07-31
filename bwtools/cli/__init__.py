import click
import sys
from .. import __version__

# CONTEXT_SETTINGS = {
#     "help_option_names": ["-h", "--help"],
# }
@click.group()
def cli(): 
    pass

# @click.version_option(__version__, "-V", "--version")
# @click.group(context_settings=CONTEXT_SETTINGS)
# @click.option(
#     "-v", "--verbose",
#     help="Verbose logging",
#     is_flag=True,
#     default=False
# )
# @click.option(
#     "-d", "--debug",
#     help="Post mortem debugging",
#     is_flag=True,
#     default=False
# )
# def cli(verbose, debug):
#     """
#     Type -h or --help after any subcommand for more information.
#     """
#     if verbose:
#         pass
#         # logger.setLevel(logging.DEBUG)

#     if debug:
#         import traceback

#         try:
#             import ipdb as pdb
#         except ImportError:
#             import pdb

#         def _excepthook(exc_type, value, tb):
#             traceback.print_exception(exc_type, value, tb)
#             print()
#             pdb.pm()

#         sys.excepthook = _excepthook


from . import (
    call_domains,
    compute_regions,

)