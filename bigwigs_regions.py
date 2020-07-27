import numpy as np
import pandas as pd
import bioframe as bf
import bbi

def regions_mean(bigwig, bed):
    stack={}
    
    for i in bed:
        df = pd.read_csv({i}, sep='\t', header=None, usecols=[0,1,2])
        
        for j in bigwig:
            stack[i,j] = np.nanmean(bbi.stackup(j, df['0'], df['1'], df['2'], bins=1))
    return stack

def df_regions_mean(df, cols, bed):    
    stack={}
    for i in bed:

        df_bed = pd.read_csv(i, sep='\t', header=None, usecols=[0,1,2], names=['chrom', 'start', 'end'])
        overlap = bf.overlap(df_bed, df)
        
        for j in cols:
            stack[i,j] = overlap[j+'_2'].mean()
        
    return stack

def df_regions_mean_list(df, cols, bed):    
    listoflists=[]
    for i in bed:
        a=[]
        df_bed = pd.read_csv(i, sep='\t', header=None, usecols=[0,1,2], names=['chrom', 'start', 'end'])
        overlap = bf.overlap(df_bed, df)
        
        for j in cols:
            a.append(overlap[j+'_2'].mean())
        listoflists.append(a)
    return listoflists

def create_plotarray(stack, cols, bed):
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