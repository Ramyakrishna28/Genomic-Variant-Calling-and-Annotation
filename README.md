# Genomic-Variant-Calling-and-Annotation
This repository contains scripts and tools for performing genomic variant calling, annotation, and analysis for obesity-related genetic studies. The workflow involves quality control, trimming, alignment, variant calling, and annotation of variants based on multiple databases such as RefSeq, Ensembl, ClinVar, and dbSNP.

Workflow Overview
Setup the Environment:

Create a Conda environment for the workflow.
Install necessary dependencies including FastQC, Trimmomatic, BWA, Samtools, GATK, and ANNOVAR.
Quality Control (FastQC):

Run FastQC to assess the quality of raw sequencing data (FASTQ files).
Generate a detailed quality report for each sample.
Trimming (Trimmomatic):

Perform read trimming to remove adapters and low-quality bases using Trimmomatic.
Alignment (BWA):

Build a reference genome index using BWA.
Align the trimmed reads to the reference genome using BWA MEM.
Post-Alignment (Samtools):

Convert the SAM files to BAM format.
Sort and index the BAM files for downstream analysis.
Perform QC checks on the BAM files using Samtools flagstat.
Variant Calling (GATK):

Prepare the reference genome using Samtools and Picard.
Use GATK HaplotypeCaller to call variants from aligned BAM files.
Output the variant calls in VCF format.
Variant Annotation (ANNOVAR):

Convert VCF files to ANNOVAR input format.
Annotate variants with gene names, disease associations, and known SNPs from RefSeq, Ensembl, ClinVar, and dbSNP databases.
Output annotated variants in a comprehensive table format.
