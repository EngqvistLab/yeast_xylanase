#### Folder containing cleaned/final data for figures/visualizations

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
