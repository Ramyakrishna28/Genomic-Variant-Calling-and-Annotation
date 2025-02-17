#install GATK
wget https://github.com/broadinstitute/gatk/releases/download/4.4.0.0/gatk-4.4.0.0.zip

#unzip the   GATK
unzip gatk-4.4.0.0.zip

#Navigate to the GATK directory:
cd gatk-4.4.0.0

(a) Index the Reference FASTA File
samtools faidx /mnt/c/Users/lenov/Downloads/genomics_obesity/Homo_sapiens.GRCh38.dna.primary_assembly.fa

(b) Create a Sequence Dictionary
./gatk CreateSequenceDictionary -R /mnt/c/Users/lenov/Downloads/genomics_obesity/Homo_sapiens.GR

(c)Index the New BAM File
samtools index /mnt/c/Users/lenov/Downloads/genomics_obesity/SRR5936734_sorted_rg.bam

(d)Run GATK 
./gatk HaplotypeCaller \
   -R /mnt/c/Users/lenov/Downloads/genomics_obesity/Homo_sapiens.GRCh38.dna.primary_assembly.fa \
   -I /mnt/c/Users/lenov/Downloads/genomics_obesity/SRR5936734_sorted_rg.bam \
   -O /mnt/c/Users/lenov/Downloads/genomics_obesity/SRR5936734_variants.vcf \
   -ERC GVCF \
   --sample-name SRR5936734

#output:SRR5936734_variants.vcf
