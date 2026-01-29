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

