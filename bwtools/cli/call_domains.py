from .. import hmm
import multiprocessing as mp
import sys

import click
from . import cli

@cli.command()
@click.option(
    "--genome", "-g",
    help="Genome assembly for chrom sizes (i.e. hg38) ",
    type=str,
    required=True,
)
@click.option(
    "--num-states", "-n",
    help="Number of HMM states",
    default=2,
    show_default=True,
    type=int
)
@click.option(
    "--cmap",
    help="Colormap to map states to colorsNumber of eigenvectors to compute.",
    type=str,
    default='coolwarm',
    show_default=True,
)

@click.option(
    "--output", "-o", 
    help="output filename (endswith:#_state_HMM.bed).",
    type=str,
    required=True,
)
@click.option(
    "--sparse", is_flag=True, 
    help="Merge neigboring bins of the same state (reduce filesize, unequal binsize)",
)
@click.option(
    "--nproc",
    "-p",
    help="Number of processes to split the work between."
    "[default: 1, i.e. no process pool]",
    default=1,
    type=int,
)
# @click.option(
#     "-v", "--verbose",
#     help="Enable verbose output",
#     is_flag=True,
#     default=False
# )
@click.argument(
    'bigwig',
    type=str,
)
def call_domains(
    input, num_states, genome, cmap, output, sparse, nproc,
):
    """Call domains using HMMs.
    """     
    chroms = hmm.get_chroms(genome)

    # execution details
    if nproc > 1:
        pool = mp.Pool(nproc)
        map_ = pool.map
    else:
        map_ = map

    #read and create dataframe from bigwig file    
    df = hmm.create_df(inputfile=input, chroms=chroms)
    
    #HMM
    for c in df.chrom:
        print('Starting HMM on ', c)
        df = hmm.hmm(df[c], num_states)
        if sparse:
            df_sparse = hmm.sparse(df)
            return df_sparse
        else:
            return df

    #write to file         
    print("Starting to write to file")
    hmm.write_to_file(df_sparse, output, num_states, cmap=cmap)
