# ***PANDriver***

A deep neural network based method that attempts to distinguish cancer driver from passenger mutations across PAN cancer. It uses associated protein's sequence, AlphaFold predicted structures, network, PSSM, and conservation based features.
---

## Repository Structure

```text
.
├── Models/                         # Saved pretrained models (per cancer type)
├── Datasets/
│   ├── BLCA.csv/              # Example input files
│   └── BRCA.csv/             # Example outputs (optional)
├── scripts/
│   ├── feature_calculation.py      # Main feature engineering pipeline
│   ├── run_inference.py            # Run predictions using saved models
│   └── utils.py                    # Helper functions
├── requirements.txt                # Provides information on the required tools for feature calculation
└── README.md

## How to run feature_calculation.py on a sample dataset
python scripts/feature_calculation.py \
  --input data/example_input/mutations.csv \
  --output data/example_output/features.csv \
  


