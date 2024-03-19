
# Cerate a set of reference alleles
cat ../*.bim | sort | uniq -c | grep -E -v "0\W[ATCG]$" | sort -r | cut -f 2,5  | sort -u -k1,1 > ref_alleles.txt


# Get only controls
fb=../bdWTC;
plink --bfile ${fb} --keep <(grep -E "FAM_58C|FAM_NBS" ${fb}.fam) --make-bed --out controlWTC --reference-allele ref_alleles.txt

# Get datasets with no controls
for f in ../*.bim 
do 
    fb=`echo $f |  sed 's/\.bim//'`
    fb_out=`basename $f .bim`
    plink --bfile ${fb} --remove <(grep -E "FAM_58C|FAM_NBS" ${fb}.fam) --make-bed --out ${fb_out}_nocontrol --reference-allele ref_alleles.txt
done 

# Get a list of all the new datasets
ls *control*.fam | sed 's/.fam//g' | grep -v "controlWTC" > allfiles.txt

# make a single dataset with all 

#First merge, get list of strand flipped SNPs
plink --bfile controlWTC --merge-list allfiles.txt --make-bed --out WTCCC_7_merged


mv ./WTCCC_7_merged.bim ./WTCCC_7_merged.bim_old
python ../map_wtccc_affy500K_to_rs/map_wtccc_affy500K_to_rs.py ./WTCCC_7_merged.bim_old <(cat ../map_wtccc_affy500K_to_rs/Affy-*-Build36-strand.txt) ./WTCCC_7_merged.bim

plink --bfile WTCCC_7_merged --exclude <(grep "\-\-\-" ./WTCCC_7_merged.bim | cut -f 2) --make-bed --out WTCCC_7_merged_clean
sed 's/^\([a-zA-Z0-9]\+\)_\([a-zA-Z0-9]\+\)/\1-\2/g' WTCCC_7_merged.fam > WTCCC_7_merged_clean.fam

