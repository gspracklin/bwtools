import pandas as pd
import numpy as np
import bioframe as bf
from .. import regions

import click
from .util import TabularFilePath, sniff_for_header
from . import cli


@cli.command()
@click.argument(
    "cool_path",
    metavar="COOL_PATH",
    type=str
)
@click.option(
    "--reference-track",
    help="Reference track for orienting and ranking eigenvectors",
    type=TabularFilePath(exists=True, default_column_index=3),
)
@click.option(
    "--contact-type",
    help="Type of the contacts perform eigen-value decomposition on.",
    type=click.Choice(["cis", "trans"]),
    default="cis",
    show_default=True,
)
@click.option(
    "--n-eigs",
    help="Number of eigenvectors to compute.",
    type=int,
    default=3,
    show_default=True,
)
@click.option(
    "-v", "--verbose",
    help="Enable verbose output",
    is_flag=True,
    default=False
)
@click.option(
    "-o", "--out-prefix",
    help="Save compartment track as a BED-like file.",
    required=True,
)
@click.option(
    "--bigwig",
    help="Also save compartment track as a bigWig file.",
    is_flag=True,
    default=False,
)