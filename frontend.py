# ===============================
# 🌸 frontend.py (Final Version)
# ===============================

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ===============================
# Load Models and Scaler
# ===============================
try:
    scaler = joblib.load("scaled_ab570.pkl")
    model = joblib.load("scaled_ab570.pkl")  # Placeholder if model same
except Exception as e:
    st.error(f"❌ Error loading model/scaler: {e}")
    st.stop()

# ===============================
# Streamlit UI
# ===============================
st.set_page_config(page_title="Flower Drying Time Predictor 🌺", layout="wide")

st.title("🌸 Flower Drying Time Prediction Dashboard")
st.markdown("Use this tool to estimate drying time based on floral traits and nectar properties.")

# Sidebar info
st.sidebar.header("**Features used (12):**")
st.sidebar.write("""
1. flowering_start  
2. flowering_end  
3. flowering_times  
4. flowers_m2  
5. nectar_ml  
6. sugar_concentration_mol  
7. sugar_concentration_perc  
8. nectar_sugar_content_mg  
9. pollen_mg  
10. corolla_mm  
11. protein  
12. sugar_perc  
""")

# ===============================
# Input Section
# ===============================
st.header("🌿 Input Flower Data")

feature_names = [
    "flowering_start", "flowering_end", "flowering_times", "flowers_m2",
    "nectar_ml", "sugar_concentration_mol", "sugar_concentration_perc",
    "nectar_sugar_content_mg", "pollen_mg", "corolla_mm", "protein", "sugar_perc"
]

input_data = {}
cols = st.columns(3)

for i, feature in enumerate(feature_names):
    with cols[i % 3]:
        input_data[feature] = st.number_input(f"{feature.replace('_', ' ').capitalize()}", value=0.0, step=0.1)

# ===============================
# Prediction Section
# ===============================
if st.button("🔮 Predict Drying Time"):
    try:
        input_df = pd.DataFrame([input_data])

        # Debug: show feature count
        st.write(f"🔹 Input shape: {input_df.shape}")
        st.write(f"🔹 Scaler expects: {scaler.n_features_in_} features")

        # Scale the input
        scaled_input = scaler.transform(input_df)

        # Placeholder "prediction"
        drying_time = np.mean(scaled_input) * 10  # Dummy logic for now

        # Classify condition based on mean feature
        if drying_time < 0:
            condition = "🌵 Dry Environment (Quick Drying)"
            color = "orange"
        elif 0 <= drying_time <= 5:
            condition = "🌤️ Moderate (Balanced Moisture)"
            color = "green"
        else:
            condition = "💧 Humid Environment (Slow Drying)"
            color = "blue"

        # Display
        st.subheader("🪻 Prediction Results")
        st.metric(label="Estimated Drying Time (proxy units)", value=f"{drying_time:.2f}")
        st.markdown(f"**Condition:** <span style='color:{color}'>{condition}</span>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")

# ===============================
# Footer
# ===============================
st.markdown("---")
st.markdown("💡 *Team : Qubit Crew*")
