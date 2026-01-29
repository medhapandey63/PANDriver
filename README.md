# PANDriver
A method that attempts to distinguish cancer driver from passenger mutations, using machine learning methods and making use of AlphaFold structures as predictive features across cancer types.

# Cancer-Specific Driver vs Passenger Mutation Classification

This repository contains scripts and pretrained cancer-specific machine learning models to classify **driver vs passenger mutations** using protein sequence-, structure-, conservation-, and network-based features.

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

