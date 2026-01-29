# PANDriver

A deep neural network based method that attempts to distinguish cancer driver from passenger mutations across PAN cancer. It uses associated protein's sequence, AlphaFold predicted structures, network, PSSM, and conservation based features.
---

## Repository Structure

```text
.
├── models/                         # Saved pretrained models (per cancer type)
├── data/
│   ├── example_input/              # Example input files
│   └── example_output/             # Example outputs (optional)
├── scripts/
│   ├── feature_calculation.py      # Main feature engineering pipeline
│   ├── run_inference.py            # Run predictions using saved models
│   └── utils.py                    # Helper functions
├── requirements.txt
└── README.md

1) Data Processing / Input Format
To run the pipeline, your dataset should contain (at minimum):
UniProt ID (e.g., P38398)
Mutation in protein notation (e.g., R175H)
Protein sequence (FASTA or as a column)
Structure information (PDB/AlphaFold structure or path to structure file)
Expected Input Columns (example)
Column	Description	Example
uniprot_id	UniProt accession	P04637
mutation	AA substitution	R175H
sequence	Protein sequence	MEEPQSDPSV...
structure_path	Path to structure file	structures/P04637.pdb
If your pipeline fetches sequences/structures automatically, clarify that here and specify what is optional vs required.
2) Prerequisites: Feature Calculation
Before running the models, you must compute features using:
scripts/feature_calculation.py
This script calculates sequence-, structure-, and network-based features required by the pretrained models.
Feature Modules / Dependencies
The feature generation depends on the following tools/resources:
protinter (protein interaction / interface-related features)
psiCDHit (sequence clustering / homolog processing)
AACon (conservation-based features)
PSSM (position-specific scoring matrix features)
IUPred2A (disorder prediction features)
pLDDT (structure confidence features, e.g., AlphaFold)
biographs (graph/network-based structural features)
Note: Some tools require separate installation and/or external databases (e.g., BLAST databases for PSSM). See below.

