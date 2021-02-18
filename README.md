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


The Notebooks are abundantly annotated and should hopefully be self-explanatory. All data files needed to carry out the analysis and produce the related publication figures are included in the repository, except for external sequence data files which need to be downloaded from a Figshare data repository (DOI: 10.6084/m9.figshare.5854692; https://figshare.com/articles/Tempo_and_mode_of_genome_evolution_in_the_budding_yeast_subphylum/5854692), and are described in the original publication (https://doi.org/10.1016/j.cell.2018.10.023). The download should be carried out automatically when running the notebooks. **A pre-requisite for this** is that your system has `wget` and `unzip` installed (typically available in Unix systems). An alternative is to manually download the files and extract them.

### Output file
The main output file is the `332_yeast_genomes_enzyme_info_version_3.tsv` tab-separated output file (found in the `/data/final/` folder).

### Project Organization
    ├── LICENSE
    ├── README.md                    <- The top-level README
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
    │   │   ├── hmm_output           <- Folder holding output from HMMER
    │   │   ├── signalp_output       <- Folder holding output from SignalP
    │   │   └── tempo_in_genome      <- Folder holding processed sequence data
    │   │
    │   └── raw_external             <- Folder holding raw unmodified experimental data
    │       ├── dbcan                <- Folder holding the dbCAN hmm models
    │       ├── phylo_tree           <- Folder holding the phylogenetic tree files
    │       └── tempo_in_genome      <- Folder holding raw sequence data
    │
    └── doc                          <- Folder holding accessory information
