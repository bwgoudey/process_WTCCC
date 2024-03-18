import pytest
from 

def test_update_bim_file():
    # Sample data for bim and annotation DataFrames
    bim_data = {'chr': [0, 0], 'id': ['SNP_A-2239604', 'SNP_A-1963219'], 'misc1': [0, 0], 'pos': [0, 0], 'allele1': ['A', 'A'], 'allele2': ['T', 'T']}
    annotation_data = {'Probe Set ID': ['SNP_A-2239604', 'SNP_A-1963219'], 'dbSNP RS ID': ['rs123456', 'rs7891011'], 'Chromosome': [1, 2], 'Physical Position': [123456, 789101], 'Strand': ['+', '-']}
    bim_df = pd.DataFrame(bim_data)
    annotation_df = pd.DataFrame(annotation_data)

    updated_bim_df = update_bim_file(bim_df, annotation_df)

    expected_output = {'chr': [1, 2], 'id': ['rs123456', 'rs7891011'], 'misc1': [0, 0], 'pos': [0, 0], 'allele1': ['A', 'A'], 'allele2': ['T', 'T']}
    expected_df = pd.DataFrame(expected_output)

    assert updated_bim_df.equals(expected_df), "The updated BIM DataFrame does not match the expected output."

