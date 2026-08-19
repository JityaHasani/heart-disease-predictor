# Heart Disease Predictor

A machine learning web app that predicts heart disease risk based on health metrics. Built as a learning project to understand ML model implementation, Streamlit web development, and deployment workflows.

> **Note:** This project was developed with AI assistance. I helped debug terminal issues, file path errors, and deployment steps. The goal was to learn how ML models are trained, how they integrate with web interfaces, and how projects are deployed to production — not to build something from scratch solo.

---

## What I Learned

- How **Logistic Regression** works and how to train it with scikit-learn
- How to turn a trained model into a **working web app** using Streamlit
- How to **deploy Python projects** to GitHub and Streamlit Cloud
- How data flows from user input → model prediction → displayed result
- File structuring, requirements management, and version control basics

---

## Features

- 13 health input fields (age, blood pressure, cholesterol, chest pain type, etc.)
- Real-time prediction using Logistic Regression
- Confidence percentage for each prediction
- Clean, responsive Streamlit interface
- Free deployment via Streamlit Cloud

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web interface (no HTML/CSS needed) |
| scikit-learn | Machine learning (Logistic Regression) |
| pandas | Data handling (CSV reading) |
| NumPy | Array operations |
| joblib | Model saving/loading |

---

## Project Structure

```
heart-disease-predictor/
├── app.py              # Streamlit web app (main interface)
├── train_model.py      # ML model training script
├── heart.csv           # Dataset (303 patient records)
├── model.pkl           # Trained model file
├── requirements.txt    # Python dependencies
├── MIND_MAP.md         # Visual flow explanation
└── GUIDE.md            # Step-by-step guide
```

---

## How It Works

1. **User enters health data** — age, sex, blood pressure, cholesterol, chest pain type, etc.
2. **Model processes the input** — Logistic Regression analyzes 13 health features
3. **Prediction is made** — outputs 0 (no disease) or 1 (has disease) with confidence %
4. **Result displayed** — green box (healthy) or red box (at risk) with probability

---

## How to Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the model (run once)
```bash
python train_model.py
```

### 3. Run the web app
```bash
streamlit run app.py
```

Opens at **http://localhost:8501**

---

## Deployment

This project is deployed on **Streamlit Cloud** (free tier).

### Steps:
1. Create a GitHub repository
2. Upload project files (app.py, train_model.py, heart.csv, model.pkl, requirements.txt)
3. Go to [share.streamlit.io](https://share.streamlit.io)
4. Connect your GitHub repo
5. Set main file to `app.py`
6. Deploy

---

## Dataset

The model is trained on a heart disease dataset with **303 patient records** and **13 features**:

| Feature | Description |
|---|---|
| age | Age in years |
| sex | 0 = Female, 1 = Male |
| cp | Chest pain type (0-3) |
| trestbps | Resting blood pressure (mm Hg) |
| chol | Cholesterol (mg/dl) |
| fbs | Fasting blood sugar > 120 (0/1) |
| restecg | Resting ECG results (0-2) |
| thalach | Maximum heart rate |
| exang | Exercise-induced angina (0/1) |
| oldpeak | ST depression |
| slope | ST segment slope (0-2) |
| ca | Number of major vessels (0-3) |
| thal | Thalassemia type (0-3) |

---

## Model Performance

- **Algorithm:** Logistic Regression
- **Accuracy:** ~93%
- **Training samples:** 242
- **Testing samples:** 61

---

## Disclaimer

This is an **educational project only**. It is not a medical diagnostic tool. Always consult a qualified healthcare professional for medical advice.

---

## Acknowledgements

- [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+disease)
- [Streamlit Documentation](https://docs.streamlit.io)
- [scikit-learn Documentation](https://scikit-learn.org)
- AI assistance for code generation and debugging
