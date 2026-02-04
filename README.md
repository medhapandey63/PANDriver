# PANDriver

PANDriver is a deep neural network based method that attempts to distinguish cancer driver from passenger mutations across PAN cancer. It uses associated protein's sequence, AlphaFold predicted structures, network, PSSM, and conservation based features. We have developed a webserver PANDriver for the overall usage with the relevant Cancer Census Genes and can be accessed at https://web.iitm.ac.in/bioinfo2/PANDriver/.

---

## Repository Structure

```text
.
├── Models/                         # Saved pretrained models (per cancer type)
├── Datasets/
│   ├── BLCA.csv/              # Example input files
│   └── BRCA.csv/             # Example outputs (optional)
├── scripts/
│   ├── feature_calculation.ipynb      # Main feature engineering pipeline
│   ├── run_inference.py            # Run predictions using saved models
│   └── utils.py                    # Helper functions
├── requirements.txt                # Provides information on the required tools for feature calculation
└── README.md

```
---

## Prerequisites: Feature Calculation
  Before running the models, you must compute features using:
  scripts/feature_calculation.py
  This script calculates sequence-, structure-, and network-based features required by the pretrained models.

    Feature Modules / Dependencies
      The feature generation depends on the following tools/resources:
        1. protinter (protein interaction / interface-related features): https://github.com/Ax-Sch/protinter 
        2. AACon (conservation-based features)
        3. PSSM (position-specific scoring matrix features)
        4. IUPred2A (disorder prediction features)
        5. pLDDT (structure confidence features, e.g., AlphaFold)
        6. [biographs](https://github.com/username/biographs) (graph/network-based structural features)
    Note: Some tools require separate installation and/or external databases (e.g., BLAST databases for PSSM). See below.

## How to run feature_calculation.py on a sample dataset

python scripts/feature_calculation.py \
  --input input_data/input.csv \
  --output output_data/complete_dataset_with_features.csv \
  --data_dir data

## How to run run_inference.py on a sample feature set

python run_inference.py \
  --cancer_type BRCA \
  --input_csv output_data/complete_dataset_with_features.csv
  


