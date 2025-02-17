#Convert VCF to ANNOVAR Input Format
perl /mnt/c/Users/lenov/Downloads/genomics_obesity/annovar/convert2annovar.pl -format vcf4 \
/mnt/c/Users/lenov/Downloads/genomics_obesity/SRR5936734_variants.vcf \
> /mnt/c/Users/lenov/Downloads/genomics_obesity/SRR5936734_variants.avinput

# Update chromosome names in place 
sed -i 's/^NC_000001.11/chr1/; s/^NC_000002.12/chr2/; s/^NC_000003.12/chr3/; s/^NC_000004.12/chr4/; s/^NC_000005.10/chr5/; s/^NC_000006.12/chr6/; s/^NC_000007.14/chr7/; s/^NC_000008.11/chr8/; s/^NC_000009.12/chr9/; s/^NC_000010.11/chr10/; s/^NC_000011.10/chr11/; s/^NC_000012.12/chr12/; s/^NC_000013.11/chr13/; s/^NC_000014.9/chr14/; s/^NC_000015.10/chr15/; s/^NC_000016.10/chr16/; s/^NC_000017.11/chr17/; s/^NC_000018.10/chr18/; s/^NC_000019.10/chr19/; s/^NC_000020.11/chr20/; s/^NC_000021.9/chr21/; s/^NC_000022.11/chr22/; s/^NC_000023.11/chrX/; s/^NC_000024.10/chrY/' "$input_file"

#Download Required Databases
cd C:\Users\lenov\Downloads\genomics_obesity\annovar

# Download RefSeq (Gene Names)
perl annotate_variation.pl -buildver hg38 -downdb -webfrom annovar refGene humandb/

# Download Ensembl (Alternative Gene Names)
perl annotate_variation.pl -buildver hg38 -downdb -webfrom annovar ensGene humandb/

# Download ClinVar (Disease Associations)
perl annotate_variation.pl -buildver hg38 -downdb -webfrom annovar clinvar_20140902 humandb/

# Download dbSNP (Known SNPs)
perl annotate_variation.pl -buildver hg38 -downdb -webfrom annovar avsnp150 humandb/

##Run ANNOVAR
# Run ANNOVAR with updated ClinVar database 
perl table_annovar.pl "$input_file" humandb/ \ -buildver hg38 -out SRR5936734_annotated \ -remove -protocol refGene,clinvar_20240611 -operation g,f -nastring .
