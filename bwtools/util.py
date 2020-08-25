def read_bed(bed):
    df_bed = pd.read_csv(bed, sep='\t', header=None, usecols=[0,1,2], names=['chrom', 'start', 'end'])
    return df_bed