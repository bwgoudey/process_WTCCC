#!/bin/python

"""Usage: script.py <bim_file> <annotation_file> <output_file>

Arguments:
  bim_file        Path to the BIM file that needs to be updated.
  annotation_file Path to the annotation file containing the new identifiers and chromosome numbers.
  output_file     Path for saving the updated BIM file.
    
"""

import pandas as pd
from docopt import docopt
from tqdm import tqdm

def update_bim_file(bim_df, annotation_df):
    annotation_dict = annotation_df.set_index('Probe Set ID')[['dbSNP RS ID', 'Chromosome']].to_dict('index')
    tqdm.pandas(desc="my bar!")

    def update_row(row):
        if row['id'] in annotation_dict:
            return pd.Series([annotation_dict[row['id']]['Chromosome'], annotation_dict[row['id']]['dbSNP RS ID'], row['misc1'], row['pos'], row['allele1'], row['allele2']])
        return row

    updated_bim_df = bim_df.progress_apply(update_row, axis=1)
    return updated_bim_df


def main(args):
    bim_file_path = args['<bim_file>']
    annotation_file_path = args['<annotation_file>']
    output_file_path = args['<output_file>']

    print("Reading BIM file")
    bim_df = pd.read_csv(bim_file_path, sep='\t', header=None, names=['chr', 'id', 'misc1', 'pos', 'allele1', 'allele2'])
    print("Reading annotation file")
    annotation_df = pd.read_csv(annotation_file_path, sep='\t', header=0)

    print("Updating BIM file")
    updated_bim_df = update_bim_file(bim_df, annotation_df)

    # Print the updated DataFrame to screen
    updated_bim_df.to_csv(output_file_path, sep='\t', header=False, index=False)

if __name__ == "__main__":
    arguments = docopt(__doc__)
    main(arguments)

