from .. import hmm

import click
#from .util import TabularFilePath, sniff_for_header
from . import cli


@cli.command()
@click.argument(
   "--input", "-i",
    help="Bigwig file to call domains on",
    #type=TabularFilePath(exists=True, default_column_index=4),
    required=True,
)
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
# @click.option(
#     "-v", "--verbose",
#     help="Enable verbose output",
#     is_flag=True,
#     default=False
# )

def call_domains(
    input, num_states, genome, cmap, output 
):
    """Call domains using HMMs.

    Args:
        input : bigwig file
        num_states : number of HMM states           
        genome ([type]): [description]
        cmap ([type]): [description]
        output ([type]): [description]
    """     
    print("Starting HMM on " + input)
    chroms = hmm.get_chroms(genome)
    df = hmm.create_df(inputfile=input, chroms=chroms)
    df = hmm.hmm(df, num_states)
    print("Finished hmm!")
    df_sparse =hmm.sparse(df)
    hmm.write_to_file(df_sparse, output, num_states, cmap=cmap)
    # df_final=merge_different_hmmstates(df_sparse, cLAD=cLAD, open=open_state)
    # df_final.to_csv(output+'_combined_state.bed', sep='\t', header=False, index=False)
    # print("write first file")
    # df_sparse[df_sparse["state"] == 0].to_csv(
    #     output + "_0_state.bed", sep="\t", header=False, index=False
    # )
    # df_sparse[df_sparse["state"] == 1].to_csv(
    #     output + "_1_state.bed", sep="\t", header=False, index=False
    # )
    # df_sparse[df_sparse["state"] == 2].to_csv(
    #     output + "_2_state.bed", sep="\t", header=False, index=False
    # )
    print("Finished writing to file")