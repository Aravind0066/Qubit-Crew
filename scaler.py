# ===============================
# scaler.py (final)
# ===============================

import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# --- Step 1: Load dataset ---
data = pd.read_csv("augmented_500.csv")
print("✅ Dataset loaded:", data.shape)

# --- Step 2: Select only numeric input columns for model ---
feature_cols = [
    "flowering_start", "flowering_end", "flowering_times", "flowers_m2",
    "nectar_ml", "sugar_concentration_mol", "sugar_concentration_perc",
    "nectar_sugar_content_mg", "pollen_mg", "corolla_mm", "protein", "sugar_perc"
]

data = data[feature_cols]
print("🧮 Using features:", data.columns.tolist())
print("✅ Shape after filtering:", data.shape)

# --- Step 3: Scale the selected features ---
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

joblib.dump(scaler, "scaled_ab570.pkl")
print("💾 Saved scaler as scaled_ab570.pkl")

# --- Step 4: Save scaled data (optional, for checking) ---
pd.DataFrame(scaled_data, columns=feature_cols).to_csv("scaled_data.csv", index=False)
print("💾 Scaled data saved as scaled_data.csv")

print("🎯 Scaling completed successfully!")
