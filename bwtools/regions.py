#!/usr/bin/env python
import numpy as np
import pandas as pd
import bioframe as bf
import bbi

def regionsTwolists(bigwig, bed):
    """Take list of bigwigs and bedfiles are calculate average signal

    Args:
        bigwig ([type]): bigwig file (chrom, start, stop, value)
        bed ([type]): bed file (chrom, start, end), only uses first 3 columns

    Returns:
        stack: dictionary of {bigwig, bed : mean}
    """
    stack={}

    for i in bed:
        df = pd.read_csv(i, sep='\t', header=None, usecols=[0,1,2])

        for j in bigwig:
            stack[i,j] = np.nanmean(bbi.stackup(j, df[0], df[1], df[2], bins=1))
    return stack

def regionsTwodf(df, cols, bed): 
    """Calculates mean on two dataframes

    Args:
        df (dataframe): bigwig dataframe
        cols (list): list of headers to use
        bed (dataframe): chrom, start, end required

    Returns:
        stack: dictionary of means
    """
    stack={}
    for i in bed:

        df_bed = pd.read_csv(i, sep='\t', header=None, usecols=[0,1,2], names=['chrom', 'start', 'end'])
        overlap = bf.overlap(df_bed, df)
        
        for j in cols:
            stack[i,j] = overlap[j+'_2'].mean()
        
    return stack

def regionsOnedf(df, cols, bed):
    """Create list of means

    Args:
        df (pandas dataframe): requires chrom, start, end
        cols (list): column headers to use for overlap
        bed (list): list of bedfiles

    Returns:
        list: ndarray of overlaps
    """
    listoflists=[]
    for i in bed:
        a=[]
        df_bed = pd.read_csv(i, sep='\t', header=None, usecols=[0,1,2], names=['chrom', 'start', 'end'])
        overlap = bf.overlap(df_bed, df)
        df_regions_mean
        for j in cols:
            a.append(overlap[j+'_2'].mean())
        listoflists.append(a)
    return listoflists

def create_plotarray(stack, bigwig):
    nd=[]
    for i in bigwig:
        nd.append(lookup(stack, i))
    return nd

def lookup(dict, keyword):
    plotarray = []
    for key, value in dict.items():
        if keyword in key:
            plotarray.append(value)
    return plotarray

def plot(ndarray, col_names, row_names,output=None):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    im = ax.imshow(ndarray)

    ax.set_xticks(np.arange(len(col_names)))
    ax.set_yticks(np.arange(len(row_names)))
    ax.set_xticklabels(col_names)
    ax.set_yticklabels(row_names)

    plt.setp(ax.get_xticklabels(), ha="right", rotation=45,
             rotation_mode="anchor")

    fig.tight_layout()
    plt.colorbar(im)
    if output != None:
        plt.savefig(output)