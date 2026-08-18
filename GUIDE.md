# Heart Disease Predictor - Complete Guide

## Project Structure

```
heart-disease-predictor/
├── MIND_MAP.md          <- Read this FIRST (understands the flow)
├── heart.csv            <- Dataset (303 patient records)
├── train_model.py       <- Trains the ML model (run once)
├── app.py               <- Streamlit web app (the interface)
├── requirements.txt     <- Python packages needed
├── model.pkl            <- Created after running train_model.py
└── GUIDE.md             <- This file (step-by-step instructions)
```

---

## Step-by-Step Instructions

### Step 1: Install Python Packages

Open a terminal/command prompt in the project folder and run:

```bash
pip install streamlit scikit-learn pandas numpy joblib
```

What this does:
- `streamlit` - Creates the web interface
- `scikit-learn` - Machine learning library (trains the model)
- `pandas` - Reads CSV files (the dataset)
- `numpy` - Handles number arrays
- `joblib` - Saves/loads the trained model

### Step 2: Train the Model (Run Once)

```bash
python train_model.py
```

What this does:
- Reads heart.csv (303 patients)
- Trains Logistic Regression model
- Tests the model (~85% accuracy)
- Saves the trained model to `model.pkl`

You should see output like:
```
Dataset loaded successfully!
Total patients: 303
Features: ['age', 'sex', 'cp', 'trestbps', ...]
Training set: 242 patients
Testing set: 61 patients
Model Accuracy: 85.2%
Model saved to 'model.pkl'!
```

### Step 3: Run the Web App

```bash
streamlit run app.py
```

What this does:
- Starts a local web server
- Opens your browser to http://localhost:8501
- Shows the Heart Disease Predictor interface

You should see:
- A web page with the title "Heart Disease Predictor"
- 13 input fields (sliders and dropdowns)
- A "Predict" button

### Step 4: Test the App

1. Fill in the form with sample data:
   - Age: 55
   - Sex: Male
   - Chest Pain: No Pain (0)
   - Blood Pressure: 140
   - Cholesterol: 280
   - Fasting Sugar: No
   - ECG Results: Normal (0)
   - Max Heart Rate: 140
   - Exercise Angina: Yes
   - ST Depression: 2.0
   - ST Slope: Flat (1)
   - Major Vessels: 2
   - Thalassemia: Normal (0)

2. Click "Predict"

3. You should see a result:
   - Green box = "No Heart Disease Detected"
   - Red box = "Heart Disease Detected"

---

## How Each File Works

### heart.csv (The Data)
- 303 rows = 303 patients
- 14 columns = 13 health metrics + 1 target (0 or 1)
- Columns: age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal, target

### train_model.py (The Training)
1. Loads CSV with pandas
2. Splits into X (inputs) and y (outputs)
3. Creates 80/20 train/test split
4. Creates LogisticRegression model
5. Trains model with model.fit()
6. Tests with model.predict()
7. Saves to model.pkl with joblib

### app.py (The Interface)
1. Loads model.pkl
2. Creates input form (sliders + dropdowns)
3. When user clicks Predict:
   - Converts text to numbers (Male->1, Female->0)
   - Creates numpy array
   - Calls model.predict()
   - Displays result

---

## Deployment to GitHub + Streamlit Cloud

### Step 1: Create GitHub Repository
1. Go to https://github.com
2. Click "New" (green button)
3. Repository name: `heart-disease-predictor`
4. Click "Create repository"

### Step 2: Upload Your Code
**Option A (Easiest - Upload via Website):**
1. On your new repo page, click "uploading an existing file"
2. Drag and drop ALL your project files:
   - heart.csv
   - train_model.py
   - app.py
   - requirements.txt
   - MIND_MAP.md
   - GUIDE.md
3. Do NOT upload model.pkl (it will be created by Streamlit Cloud)
4. Click "Commit changes"

**Option B (Using Git Commands):**
```bash
cd heart-disease-predictor
git init
git add .
git commit -m "Heart disease predictor project"
git remote add origin https://github.com/YOUR_USERNAME/heart-disease-predictor.git
git push -u origin main
```

### Step 3: Deploy on Streamlit Cloud (FREE)
1. Go to https://share.streamlit.io
2. Sign in with your GitHub account
3. Click "New app"
4. Repository: Select your repo `heart-disease-predictor`
5. Branch: `main`
6. Main file path: `app.py`
7. Click "Deploy"

### Step 4: Add Training Script to Deployment
Streamlit Cloud doesn't automatically run train_model.py. We need to add it:

1. In your deployed app, go to the app settings (Manage app)
2. Or add this to your repository: create a file named `Procfile` with:
```
web: streamlit run app.py
```

Wait, we need the model to be trained first. Let me update app.py to handle this:

Actually, the easiest solution is to **include model.pkl in your repository**:
1. Run `python train_model.py` on your computer first
2. This creates `model.pkl`
3. Upload `model.pkl` to GitHub along with other files
4. Streamlit Cloud will then have the model ready

### Step 5: Your App is Live!
- URL: `https://YOUR_USERNAME-heart-disease-predictor-app-XXXXX.streamlit.app`
- Anyone can now use your heart disease predictor
- Share the URL with your hackathon judges!

---

## Common Issues & Fixes

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Fix:** Run `pip install streamlit scikit-learn pandas numpy joblib`

### Issue: "FileNotFoundError: heart.csv"
**Fix:** Make sure you're running the script from the project folder. Use `cd` to navigate there first.

### Issue: "FileNotFoundError: model.pkl"
**Fix:** Run `python train_model.py` first to create the model file.

### Issue: Streamlit app shows error on deployment
**Fix:** Make sure:
1. `requirements.txt` is in your repository
2. `model.pkl` is in your repository (run train_model.py locally first)
3. Main file path is set to `app.py` in Streamlit Cloud settings

---

## What to Explain in Your Hackathon Presentation

### The Problem
"Heart disease is the leading cause of death worldwide. Early detection can save lives."

### The Solution
"We built a web app that predicts heart disease risk using machine learning."

### How It Works (30-second explanation)
1. User enters health data (age, blood pressure, cholesterol, etc.)
2. ML model (Logistic Regression) analyzes the data
3. Model predicts if there's heart disease risk
4. Shows result with confidence percentage

### The Tech Stack
- **Python** - Main programming language
- **Streamlit** - Web interface (no HTML/CSS needed)
- **Scikit-learn** - Machine learning library
- **Logistic Regression** - The ML algorithm

### What You Learned
- How to train a machine learning model
- How to create a web app with Streamlit
- How to deploy to GitHub and Streamlit Cloud
- How data flows from user input -> model -> prediction -> result

---

## Quick Reference Commands

```bash
# Install packages
pip install streamlit scikit-learn pandas numpy joblib

# Train model (run once)
python train_model.py

# Run app locally
streamlit run app.py

# Git commands for deployment
git init
git add .
git commit -m "Heart disease predictor"
git remote add origin https://github.com/YOUR_USERNAME/heart-disease-predictor.git
git push -u origin main
```
