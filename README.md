# Map Affymetric identifiers used in WTCCC to RS ids

This is a script to to change the identifiers for SNPs in a PLINK bim file. The old bim file is as follows:

`
0       SNP_A-2239604   0       0       A       T
0       SNP_A-1963219   0       0       A       T
0       SNP_A-2106428   0       0       T       A
0       SNP_A-2073413   0       0       T       C
0       SNP_A-2197317   0       0       T       C
0       SNP_A-2143587   0       0       A       G
0       SNP_A-4260407   0       0       G       T
0       SNP_A-1896479   0       0       T       C
0       SNP_A-2024690   0       0       T       C
0       SNP_A-4252982   0       0       G       A
`

We assume that we have an annotations for the chip (here taken from Will Raynor's site Nsp-Sty.na30-b36-strand.zip). These look as follows
`
Probe Set ID    dbSNP RS ID Chromosome  Physical Position   Strand
SNP_A-1780358   rs17325399  5   54442707    +
SNP_A-1780551   rs12454921  18  52924726    -
SNP_A-1780357   rs2713901   15  54398617    -
SNP_A-1780550   rs7965238   12  32113857    +
SNP_A-1780352   rs17012816  4   88667542    +
SNP_A-1780351   rs5995963   22  39632919    -
SNP_A-1780350   rs7785921   7   36729248    -
SNP_A-1780748   rs2776928   10  33614411    -
SNP_A-1780747   rs1108543   19  62191356    +
`

This script produces an updated BIM that  alters identifier, chromsome and
position and prints a copy of the new bim file based on the annotation file. We
make the assumption that the SNP_A-[0-9]+ identifiers are always the key. 

If the key is missing, we just leave the line as is. 



# SETUP 
Create a virtual environment. Add pre-requisite packages as follows. 
`pip install -r ./requirements.txt`


