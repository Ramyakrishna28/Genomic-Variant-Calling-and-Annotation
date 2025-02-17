#Set Up Environment
# Source the .bashrc file
source ~/.bashrc

# Create the working environment for genomics obesity analysis
conda create -n genomics_obesity
conda activate genomics_obesity

# Change the directory where the FASTQ files are stored
cd C:\Users\lenov\Downloads\genomics_obesity\data

##FASTQC
# Create a directory to save the FastQC results
mkdir -p /mnt/c/Users/lenov/Downloads/genomics_obesity/fastqc_results

# Run FastQC to check the quality of the raw data
fastqc -o /path/to/output /path/to/input.fastq

##TRIMMING
trimmomatic SE -threads 4 input.fastq output_trimmed.fastq

#Download the reference genome
wget ftp://ftp.ensembl.org/pub/release-106/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz

#unzip the reference genome 
gunzip Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz

##Reference Genome Indexing with BWA
bwa index reference_genome.fa

##Alignment with BWA MEM
bwa mem reference_genome.fa input_trimmed.fastq > aligned.sam

##Convert SAM to BAM with Samtools
samtools view -Sb aligned.sam > aligned.bam
samtools sort aligned.bam -o sorted_aligned.bam
samtools index sorted_aligned.bam

