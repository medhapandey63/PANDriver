import os
import argparse
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

# -----------------------------
# ARGUMENTS
# -----------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--cancer_type", required=True, help="e.g. BRCA, LUAD, GBM")
parser.add_argument("--input_csv", required=True, help="Input feature CSV")
args = parser.parse_args()

cancer_type = args.cancer_type.upper()
input_csv = args.input_csv

# -----------------------------
# PATHS
# -----------------------------
MODEL_PATH = f"../Models/{cancer_type}_model.h5"
FEATURE_PATH = f"../selected_features/{cancer_type}_features.txt"
OUTPUT_DIR = "../output_data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------
# LOAD MODEL
# -----------------------------
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

model = load_model(MODEL_PATH)

# -----------------------------
# LOAD FEATURES
# -----------------------------
if not os.path.exists(FEATURE_PATH):
    raise FileNotFoundError(f"Feature file not found: {FEATURE_PATH}")

with open(FEATURE_PATH) as f:
    selected_features = [line.strip() for line in f if line.strip()]

# -----------------------------
# LOAD INPUT DATA
# -----------------------------
df = pd.read_csv(input_csv)

# Check missing features
missing = set(selected_features) - set(df.columns)
if missing:
    raise ValueError(f"Missing features in input CSV: {missing}")

X = df[selected_features].values

# -----------------------------
# RUN PREDICTION
# -----------------------------
probs = model.predict(X)

# If binary classifier
if probs.shape[1] == 1:
    prob_class1 = probs.flatten()
else:
    prob_class1 = probs[:, 1]

pred_class = (prob_class1 >= 0.5).astype(int)

# -----------------------------
# OUTPUT DATAFRAME
# -----------------------------
out_df = df.copy()
out_df["Predicted_Class"] = pred_class
out_df["Probability"] = prob_class1

# -----------------------------
# SAVE OUTPUT
# -----------------------------
out_file = os.path.join(OUTPUT_DIR, f"{cancer_type}_predictions.csv")
out_df.to_csv(out_file, index=False)

print(f"Saved predictions to: {out_file}")

