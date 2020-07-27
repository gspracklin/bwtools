#!/usr/bin/env python
import numpy as np
import pandas as pd
import bioframe as bf
import bbi

def regions_mean(bigwig, bed):
    """Take list of bigwigs and bedfiles are calculate average signal

    Args:
        bigwig ([type]): bigwig file (chrom, start, stop, value)
        bed ([type]): bed file (chrom, start, end), only uses first 3 columns

    Returns:
        stack: dictionary of {bigwig, bed : mean}
    """
    stack={}
    
    for i in bed:
        df = pd.read_csv({i}, sep='\t', header=None, usecols=[0,1,2])
        
        for j in bigwig:
            stack[i,j] = np.nanmean(bbi.stackup(j, df['0'], df['1'], df['2'], bins=1))
    return stack

def df_regions_mean(df, cols, bed): 
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

def df_regions_mean_list(df, cols, bed):
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

def create_plotarray(stack, cols, bed): 
    """Converts dictionary to ndarray for plotting

    Args:
        stack (dictionary): dictionary from regions
        cols (list): all the headers or bigwigs used
        bed (list): list of bedfiles used

    Returns:
        array : numpy ndarray
    """
    b=[]
    num_cols = len(cols)
    num_rows = len(bed)
    
    #convert dictionary keys to list
    a=list(stack.values())
    
    #convert list to ndarray
    for i in range(0,num_cols,num_rows):  
        b.append(a[i:num_cols])

    return np.array(b)

def plot(ndarray, cols, bed, output=None):
    """Create matplotlib plot

    Args:
        ndarray (ndarray): list of means (bigwigs/rows, bedfile/columns)
        cols (list): name for the columns   
        bed (list): name for the rows       
        output (file name, optional): 'filename.pdf' (or png). Defaults to None.
    """
    import matplotlib.pyplot as plt
    
    fig, ax = plt.subplots()
    im = ax.imshow(ndarray)

    # We want to show all ticks...
    ax.set_xticks(np.arange(len(cols)))
    ax.set_yticks(np.arange(len(bed)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(cols)
    ax.set_yticklabels(bed)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), ha="right", rotation=45,
             rotation_mode="anchor")

    # # Loop over data dimensions and create text annotations.
    # for i in range(len(marks)):
    #     for j in range(len(subcompartments)):
    #         text = ax.text(j, i, np.array(b)[i, j],
    #                        ha="center", va="center", color="w")

#     ax.set_title("RT and E1 in heterochromatin")
    fig.tight_layout()
    plt.colorbar(im)
    if output != None:
        plt.savefig(output)