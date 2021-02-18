# CAZyme prediction in Ascomycetes yeast genomes
A bioinformatic analysis was carried out with the goal of identifying carbohydrate-active enzymes in 332 published yeast genomes.

![Figure](/figures/332_tree.png)

## Requirements and usage
The scripts in this repository are in the form of Jupyter Notebooks and rely on Python (3.7). A full list of required packages, and their versions, are included in the `./code/environment.yml` file. This file can be used as a reference to manually install the libraries using pip, but it is by far easier to make use of Miniconda (https://docs.conda.io) to create an environment with all the libraries inside.

```bash
conda env create -f environment.yml
conda env activate xylanase
```

In addition to the computational environment indicated above, SignalP (http://www.cbs.dtu.dk/services/SignalP/, version 5.0b) has to be installed manually before running the scripts in this repository.


The Notebooks are abundantly annotated and should hopefully be self-explanatory. All data files needed to carry out the analysis and produce the related publication figures are included in the repository. Additionally, the full analysis requires the downloading of data files from the Zenodo data repository (http://doi.org/10.1016/j.cell.2018.10.023). The download should be carried out automatically when running the notebooks. **A pre-requisite for this** is that your system has `wget` and `unzip` installed (typically available in Unix systems). An alternative is to manually download the files and extract them. Finally, the analysis relies on accessory code from one of our other repositories (https://github.com/EngqvistLab/tome). This will be automatically installed if using Miniconda and the environment.yml file.

### Output file description
The main output file is the "332_yeast_genomes_enzyme_info_version_3.tsv" tab-separated output file (found in the `/data/final/` folder). Each row in the data file indicated one gene with a single corresponding hmm hit at a specific position in the gene. A gene can (and often does) occur multiple times with different hmm model hits or hits with the same hmm model but at different positions inside the gene. Below follows a description of the data contained in each column of the output file. The name of each gene is specified and the corresponding protein sequence can be obtained from the organism fasta files obtained from the Zenodo repository indicated above.

**The columns in the output file `332_yeast_genomes_enzyme_info_version_3.tsv` are as follows:**

column: organism \
description: the organism name \
value type: text


column: gene \
description: the gene name as given inside fasta files \
value type: text


column: hmm_model \
description: the hmm model from signalp that gave the hit \
value type: text


column: hmm_model_len \
description: length of the hmm model, specified in the hmmer output file (there in the "qlen" column) \
value type: integer


column: hmm_match_from \
description: where in the hmm model the match with the gene starts,  specified in the hmmer output file (there in the "hmm coord from" column) \
value type: integer


column: hmm_match_to \
description: where in the hmm model the match with the gene ends,  specified in the hmmer output file (there in the "hmm coord to" column) \
value type: integer


column: hmm_match_coverage \
description: how much of hmm model actualy matched to the gene from 0.35 to 1.0, computed as ("hmm_match_to" - "hmm_match_from")/"hmm_model_len" \
value type: float


column: match_evalue \
description: the e-value of the hmm model hit, specified in the hmmer output file (there in the "Evalue" column) \
value type: float, scientific notation


column: gene_match_from \
description: where in the gene the hmm model match starts, specified in the hmmer output file (there in the "ali coord from" column) \
value type: integer


column: gene_match_to \
description: where in the gene the hmm model match ends, specified in the hmmer output file (there in the "ali coord to" column) \
value type: integer


column: enzyme \
description: the full enzyme name, parsed from the hmm model name by excluding the ".hmm" file extension \
value type: text


column: family \
description: the enzyme name, excluding subfamily designations, parsed from the "enzyme" column \
value type: text


column: enzyme_type \
description: which main class of enzyme it is, GH, CBM, CE, etc., parsed from the "family" column \
value type: text


column: signal_peptide \
description: whether signal peptide is predicted (SP(Sec/SPI)) or not (OTHER), specified in the signalp output file (there in the "Prediction" column) \
value type: text


column: signal_peptide_prob \
description: probability that a signal peptide is present, specified in the signalp output file (there in the "SP(SEC/SPI)" column) \
value type: float


column: sp_cut_pos \
description: the position in the protein sequence where the signal peptide is predicted to be cleaved, specified in the signalp output file (there in the "CS Position" column) \
value type: text


column: sp_cut_seq \
description: the sequence at which the signal peptide is predicted to be cleaved, specified in the signalp output file (there in the "CS Position" column) \
value type: text


column: sp_cut_prob \
description: the probability of the cut-site prediction, specified in the signalp output file (there in the "CS Position" column) \
value type: float


column: genes_in_fasta \
description: the number of genes present in the organisms fasta file \
value type: integer


column: pred_growth_temp(c) \
description: the organism growth temperature in centigrade (Celsius) as predicted by Tome from the fasta files \
value type: integer



### Project Organization
    ├── LICENSE
    ├── README.md                    <- The top-level README for developers using this project.
    │
    ├── code
    │   ├── 1_de-duplication_of_genes.ipynb   <- Notebook for de-duplicating fasta file genes
    │   ├── 2_analyze_genomes.ipynb           <- Notebook for predicting CAZyme domains
    │   ├── 3_phylo_tree_and_plots.ipynb      <- Notebook for making publication figures
    │   └── environment.yml                   <- File specifying the computational environment
    │
    ├── data
    │   ├── final                    <- Folder holding output files of processed data
    │   │
    │   ├── intermediate             <- Folder holding intermediate data that has been transformed
    │   │   ├── hmm_output           <- Folder
    │   │   ├── signalp_output       <- Folder
    │   │   └── tempo_in_genome      <- Folder
    │   │
    │   └── raw_external             <- Folder holding raw unmodified experimental data
    │       ├── dbcan                <- Folder
    │       ├── phylo_tree           <- Folder containing
    │       └── tempo_in_genome      <- Folder containing
    │
    └── doc                          <- Folder containing accessory information
