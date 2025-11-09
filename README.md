# Genomic-Variant-Calling-and-Annotation

This repository presents a complete Genomic Variant Calling and Annotation Pipeline for identifying and interpreting obesity-associated genetic variants using Illumina sequencing data.
The pipeline integrates preprocessing, alignment, variant calling, and annotation with multiple genomic databases for high-confidence variant interpretation.

 Pipeline Overview
🟢 Step 1: Environment Setup

A dedicated Conda environment is created to ensure reproducibility and ease of dependency management.
All required tools — FastQC, Trimmomatic, BWA, SAMtools, GATK, and ANNOVAR — are installed within the environment.

🧪 Step 2: Quality Control

Raw sequencing reads are assessed for quality using FastQC.
The generated reports provide insights into base quality, GC content, and potential adapter contamination.

✂️ Step 3: Trimming

Low-quality bases and adapter sequences are removed using Trimmomatic, ensuring high-quality reads for alignment.
This step enhances downstream variant calling accuracy.

🧬 Step 4: Reference Genome Preparation

The GRCh38 reference genome is downloaded and indexed using BWA to prepare for alignment.
This step ensures efficient and accurate mapping of trimmed reads to the reference.

🧷 Step 5: Alignment

Reads are aligned to the reference genome using BWA MEM.
The resulting SAM files are converted, sorted, and indexed into BAM format using SAMtools.
These cleaned, indexed BAM files are then used for variant discovery.

🔍 Step 6: Variant Calling

GATK HaplotypeCaller is used to identify SNPs and INDELs from aligned reads.
The generated VCF files represent the raw variant calls for each sample.
Additional indexing and dictionary creation steps ensure smooth integration with downstream tools.

🧩 Step 7: Variant Annotation

Variants are annotated using ANNOVAR with multiple databases, including:
RefSeq – Gene annotations
Ensembl – Alternative gene models
ClinVar – Disease associations
dbSNP – Known variant identifiers

The annotated results provide insights into variant impact, gene function, and clinical significance.

Key Tools & Dependencies:

| Tool                 | Role                                        |
| -------------------- | ------------------------------------------- |
| **FastQC**           | Quality assessment of raw reads             |
| **Trimmomatic**      | Adapter and low-quality read trimming       |
| **BWA**              | Alignment of reads to the reference genome  |
| **SAMtools**         | File conversion, sorting, and indexing      |
| **GATK**             | Variant discovery and filtering             |
| **ANNOVAR**          | Variant annotation and interpretation       |
| **wget / sed / awk** | Data download and file formatting utilities |

📁 Output Files
| File                                      | Description                                                  |
| ----------------------------------------- | ------------------------------------------------------------ |
| `sorted_aligned.bam`                      | Cleaned and indexed alignment file                           |
| `SRR5936734_variants.vcf`                 | Raw variant calls from GATK                                  |
| `SRR5936734_annotated.hg38_multianno.txt` | Fully annotated variant table with gene and clinical details |

