#!/bin/python

"""Usage: script.py <bim_file> <annotation_file>

Arguments:
  bim_file        Path to the BIM file that needs to be updated.
  annotation_file Path to the annotation file containing the new identifiers and chromosome numbers.

"""

import pandas as pd
from docopt import docopt

def update_bim_file(bim_df, annotation_df):
    annotation_dict = annotation_df.set_index('Probe Set ID')[['dbSNP RS ID', 'Chromosome']].to_dict('index')

    updated_rows = []
    for index, row in bim_df.iterrows():
        if row['id'] in annotation_dict:
            updated_row = row.copy()
            updated_row['id'] = annotation_dict[row['id']]['dbSNP RS ID']
            updated_row['chr'] = annotation_dict[row['id']]['Chromosome']
            updated_rows.append(updated_row)
        else:
            updated_rows.append(row)

    return pd.DataFrame(updated_rows, columns=bim_df.columns)

def main(args):
    bim_file_path = args['<bim_file>']
    annotation_file_path = args['<annotation_file>']

    bim_df = pd.read_csv(bim_file_path, sep='\t', header=None, names=['chr', 'id', 'misc1', 'pos', 'allele1', 'allele2'])
    annotation_df = pd.read_csv(annotation_file_path, sep='\t', header=0)

    updated_bim_df = update_bim_file(bim_df, annotation_df)

    # Print the updated DataFrame to screen
    updated_bim_df.to_csv(sys.stdout, sep='\t', header=False, index=False)

if __name__ == "__main__":
    arguments = docopt(__doc__)
    main(arguments)

