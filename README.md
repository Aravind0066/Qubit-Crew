# Qubit-Crew
# 🌸 Quantum Bloom — Flower Drying Time Predictor

**Quantum Bloom** is a Streamlit-powered dashboard that blends **quantum-inspired machine learning (QSVM)** with floral ecology.  
It predicts flower drying behavior using environmental and botanical parameters like **nectar concentration**, **pollen weight**, and **flower density** — beautifully merging **nature and computation**.

---

## 🧬 Inspiration

Flowers are more than beauty — they’re data.  
Their drying rate affects **pollination timing**, **nectar yield**, and even **ecosystem dynamics**.  
But traditional models struggle with the **complex, nonlinear, and quantum-like dependencies** between these traits.

That’s where **Quantum Bloom** steps in — using **quantum-enhanced Support Vector Machines (QSVM)** and **PCA-based scaling** to capture intricate floral relationships.

---

## 🌿 Project Overview

| Component | Description |
|------------|-------------|
| **Dataset** | Augmented floral dataset containing 500+ samples |
| **Model** | QSVM trained on PCA-reduced features |
| **Scaler** | StandardScaler fitted on filtered ecological traits |
| **Frontend** | Streamlit dashboard for real-time predictions |
| **Goal** | Predict time-to-dry category (Dry / Moderate / Humid) |

---

## 💡 Problem Statement

Drying time of a flower is a key ecological indicator.  
Understanding and predicting it helps:

- Forecast **flower lifespan** under climate variation  
- Optimize **nectar collection timing**  
- Assist **florists** and **agricultural researchers** in preservation strategies  

However, real-world data is scarce and nonlinear — hence, we use **augmented data + quantum-inspired kernels** for robust generalization.

---

## ⚗️ Methodology

1. **Data Preprocessing**
   - Source dataset: `augmented_500.csv`
   - Extracted 12 crucial features:
     ```
     flowering_start, flowering_end, flowering_times, flowers_m2,
     nectar_ml, sugar_concentration_mol, sugar_concentration_perc,
     nectar_sugar_content_mg, pollen_mg, corolla_mm, protein, sugar_perc
     ```

2. **Feature Scaling**
   - Scaled using `StandardScaler`  
   - Script: `scaler.py`
   - Output files:  
     ```
     scaled_ab570.pkl   # Saved scaler
     scaled_data.csv    # Scaled feature matrix
     ```

3. **Dimensionality Reduction (Optional)**
   - PCA model (`pca_model.pkl`) used for reducing redundant dimensions.

4. **QSVM Model**
   - Quantum Support Vector Machine trained on scaled and PCA-transformed data.  
   - Utilizes quantum kernels for non-linear decision boundaries.

---

## 🧠 Files & Roles

| File | Description |
|------|-------------|
| `augmented_500.csv` | Augmented dataset with ecological + nectar properties |
| `scaler.py` | Script to preprocess and generate scaler objects |
| `scaled_ab570.pkl` | Fitted scaler model |
| `scaled_data.csv` | Scaled feature data |
| `pca_model.pkl` | Trained PCA model for feature compression |
| `frontend.py` | Streamlit interface for predictions |

---

## ⚙️ How to Run Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/QuantumBloom.git
cd QuantumBloom
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Preprocess the Data
Run the scaler script first:
```bash
python scaler.py
```
This will generate:
```
scaled_ab570.pkl
scaled_data.csv
```

### 4️⃣ Ensure All Files Are in the Same Folder
Make sure your project structure looks like this:
```
📂 Streamlit/
 ┣ 📄 augmented_500.csv
 ┣ 📄 frontend.py
 ┣ 📄 scaler.py
 ┣ 📄 scaled_ab570.pkl
 ┣ 📄 scaled_data.csv
 ┣ 📄 pca_model.pkl
```

### 5️⃣ Launch the App
```bash
streamlit run frontend.py
```

---

## 🌍 Streamlit Cloud Deployment

🎯 **Deployed Live App:**  
👉 [Try Quantum Bloom on Streamlit!](https://your-streamlit-app-link.streamlit.app)  

*(replace this link with your Streamlit Cloud deployment URL)*

---

## 🎨 Features

1. **Interactive Input Panel**
   - Enter floral and nectar parameters manually.
2. **Auto Classification**
   - Detects whether the environment is **Dry**, **Moderate**, or **Humid**.
3. **Visual Feedback**
   - Color-coded environmental condition tags.
4. **Real-Time Scaling**
   - Input data is auto-transformed using your trained `scaled_ab570.pkl`.

---

## 🔬 Domain

**Quantum Machine Learning (QML)** × **Ecological Informatics**

- Demonstrates how **quantum-inspired models** can enhance pattern recognition in complex biological systems.  
- Built as part of an academic exploration into **hybrid quantum-classical ML** pipelines.

---

## 📈 Future Enhancements

- Integration with **real weather APIs** for live humidity & temperature data.  
- Replace dummy prediction logic with **actual QSVM model inference**.  
- Add **interactive visualizations** for PCA distributions.  
- Deploy on a **custom domain** for public access.

---

## 👩‍💻 Team Quantum Bloom

| Name | Role |
|------|------|
| **Aravind M** | Lead Developer, Model Architect |
| *(add teammates if any)* | Data Augmentation / Frontend / Quantum Integration |

---

## 🪻 Tech Stack

- **Python 3.12**
- **Streamlit** – Frontend framework
- **scikit-learn** – Scaler & PCA
- **PennyLane / Qiskit** – Quantum ML experiments
- **Joblib** – Model serialization

---

## 📜 License

MIT License © 2025 **Aravind M**  
Feel free to fork, modify, and cite this project in your research or hackathon submissions.

