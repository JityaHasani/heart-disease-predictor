# ====================================================================
# HEART DISEASE PREDICTOR - STREAMLIT WEB APP
# ====================================================================
# This is the user interface. When someone opens this in a browser,
# they see a nice form where they can enter their health data.
# The app sends that data to the ML model and shows the result.
#
# HOW TO RUN:
#   1. First run: python train_model.py (to create model.pkl)
#   2. Then run: streamlit run app.py
#   3. Opens in your browser at http://localhost:8501
# ====================================================================


# --------------------------------------------------------------------
# STEP 1: IMPORT LIBRARIES
# --------------------------------------------------------------------
# We need different libraries than train_model.py because this file
# creates a web interface, not trains a model.

import streamlit as st           # Streamlit: creates web apps with Python (no HTML needed!)
import numpy as np               # NumPy: helps us create arrays for the model
import joblib                    # Joblib: loads the saved model from file
import pandas as pd              # Pandas: helps us work with data
import os                        # OS: helps us find file paths

# Get the folder where this script is located (so files are found no matter where you run from)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# WHAT JUST HAPPENED:
# We loaded 4 tools:
#   - streamlit: creates the web page (inputs, buttons, text)
#   - numpy: creates the data array the model expects
#   - joblib: loads the trained model from model.pkl
#   - pandas: (we might use it for data display)
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# STEP 2: CONFIGURE THE WEB PAGE
# --------------------------------------------------------------------
# These lines set up how the page looks before anything else loads.

st.set_page_config(
    page_title="Heart Disease Predictor",    # Title shown in browser tab
    page_icon="heart",                        # Icon in browser tab
    layout="centered"                         # Content centered on page
)

# WHAT JUST HAPPENED:
# We told Streamlit:
#   - Page title = "Heart Disease Predictor"
#   - Page icon = heart emoji
#   - Layout = centered (not wide)
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# STEP 3: DISPLAY THE PAGE TITLE
# --------------------------------------------------------------------
# This is what the user sees at the top of the page.

st.title("Heart Disease Predictor")
st.markdown("Enter your health details below to check your heart disease risk.")

# WHAT JUST HAPPENED:
# We showed a big title and a description on the web page.
# st.title() creates a large heading.
# st.markdown() creates formatted text (like bold, italic, etc.)
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# STEP 4: LOAD THE TRAINED MODEL
# --------------------------------------------------------------------
# We load the model.pkl file that train_model.py created.
# If the file doesn't exist, we show an error message.

try:
    model = joblib.load(os.path.join(SCRIPT_DIR, 'model.pkl'))     # Load the trained model from file
    st.success("Model loaded successfully!")   # Show green success message
except FileNotFoundError:
    st.error("Model file not found! Please run 'python train_model.py' first.")
    st.stop()    # Stop the app if model isn't found

# WHAT JUST HAPPENED:
# We tried to load the model from 'model.pkl'.
# If it exists: great! The 'model' variable now contains the trained brain.
# If it doesn't exist: we show an error and stop.
#
# The model is the same one from train_model.py.
# It knows the patterns: "high BP + high cholesterol = risky"
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# STEP 5: CREATE INPUT FIELDS (The Form)
# --------------------------------------------------------------------
# We create a two-column layout to make the form look nice.
# Left column: first set of inputs
# Right column: second set of inputs

col1, col2 = st.columns(2)    # Split page into 2 columns

# --- LEFT COLUMN INPUTS ---
with col1:
    # Each st.slider creates a slider the user can drag
    # Parameters: label, minimum_value, maximum_value, default_value
    
    age = st.slider("Age", 20, 80, 45)
    # User drags slider to pick age (20-80), default is 45
    
    sex = st.selectbox("Sex", ["Male", "Female"])
    # User picks Male or Female from dropdown
    
    cp = st.selectbox("Chest Pain Type", [
        "Typical Angina (0)",
        "Atypical Angina (1)", 
        "Non-Anginal Pain (2)",
        "Asymptomatic (3)"
    ])
    # User picks type of chest pain (0-3)
    
    trestbps = st.slider("Resting Blood Pressure (mm Hg)", 80, 200, 120)
    # User picks blood pressure (80-200), default 120
    
    chol = st.slider("Cholesterol (mg/dl)", 100, 400, 200)
    # User picks cholesterol level (100-400), default 200
    
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["No", "Yes"])
    # User picks if blood sugar is high

# --- RIGHT COLUMN INPUTS ---
with col2:
    restecg = st.selectbox("Resting ECG Results", [
        "Normal (0)",
        "ST-T Wave Abnormality (1)",
        "Left Ventricular Hypertrophy (2)"
    ])
    # User picks ECG result (0-2)
    
    thalach = st.slider("Maximum Heart Rate", 60, 220, 150)
    # User picks max heart rate (60-220), default 150
    
    exang = st.selectbox("Exercise-Induced Angina", ["No", "Yes"])
    # User picks if they get chest pain during exercise
    
    oldpeak = st.slider("ST Depression (Oldpeak)", 0.0, 6.2, 1.0, 0.1)
    # User picks ST depression value (0-6.2), default 1.0
    
    slope = st.selectbox("ST Segment Slope", [
        "Upsloping (0)",
        "Flat (1)",
        "Downsloping (2)"
    ])
    # User picks slope type (0-2)
    
    ca = st.slider("Number of Major Vessels (0-3)", 0, 3, 0)
    # User picks number of major vessels (0-3)
    
    thal = st.selectbox("Thalassemia", [
        "Normal (0)",
        "Fixed Defect (1)",
        "Reversible Defect (2)",
        "Unknown (3)"
    ])
    # User picks thalassemia type (0-3)

# WHAT JUST HAPPENED:
# We created a form with 13 input fields:
#
# Left Column:                    Right Column:
# ┌─────────────────────┐       ┌─────────────────────┐
# │ Age: [====45====]   │       │ ECG Results: [dropdown] │
# │ Sex: [Male v]       │       │ Max Heart Rate: [===]   │
# │ Chest Pain: [dropdown]│      │ Exercise Angina: [No]   │
# │ Blood Pressure: [===]│      │ ST Depression: [==1.0==]│
# │ Cholesterol: [===]  │       │ ST Slope: [dropdown]    │
# │ Fasting Sugar: [No] │       │ Major Vessels: [0-3]    │
# └─────────────────────┘       │ Thalassemia: [dropdown] │
#                                └─────────────────────┘
#
# Each widget automatically saves its value to a variable.
# When user moves the "Age" slider, the 'age' variable updates.
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# STEP 6: CREATE THE PREDICT BUTTON
# --------------------------------------------------------------------
# When user clicks this button, the prediction code runs.

if st.button("Predict", type="primary"):
    # This code ONLY runs when the button is clicked
    # The "type=primary" makes the button blue and prominent
    
    # --- Convert user inputs to numbers the model understands ---
    # The model expects numbers, not text like "Male" or "Female"
    # So we convert: Male -> 1, Female -> 0
    
    sex_encoded = 1 if sex == "Male" else 0
    # Convert "Male"/"Female" to 1/0
    
    cp_encoded = int(cp.split("(")[-1].rstrip(")"))
    # Extract number from text like "Typical Angina (0)" -> 0
    # split("(") gives ["Typical Angina ", "0)"]
    # [-1] gives "0)"
    #rstrip(")") gives "0"
    # int() converts "0" to the number 0
    
    fbs_encoded = 1 if fbs == "Yes" else 0
    # Convert "Yes"/"No" to 1/0
    
    restecg_encoded = int(restecg.split("(")[-1].rstrip(")"))
    # Extract number from ECG text
    
    exang_encoded = 1 if exang == "Yes" else 0
    # Convert "Yes"/"No" to 1/0
    
    slope_encoded = int(slope.split("(")[-1].rstrip(")"))
    # Extract number from slope text
    
    thal_encoded = int(thal.split("(")[-1].rstrip(")"))
    # Extract number from thal text

    # WHAT JUST HAPPENED:
    # We converted all dropdown/text inputs to numbers:
    #   "Male" -> 1
    #   "Female" -> 0
    #   "Typical Angina (0)" -> 0
    #   "Atypical Angina (1)" -> 1
    #   etc.
    #
    # The model only understands numbers, so this conversion is necessary.
    # --------------------------------------------------------------------


    # --- Create the input array for the model ---
    # The model expects a specific order of features:
    # [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    
    input_data = np.array([[
        age,                # Age in years
        sex_encoded,        # 0=Female, 1=Male
        cp_encoded,         # 0-3 (chest pain type)
        trestbps,           # Blood pressure in mm Hg
        chol,               # Cholesterol in mg/dl
        fbs_encoded,        # 0=No, 1=Yes (fasting blood sugar)
        restecg_encoded,    # 0-2 (ECG results)
        thalach,            # Maximum heart rate achieved
        exang_encoded,      # 0=No, 1=Yes (exercise angina)
        oldpeak,            # ST depression value
        slope_encoded,      # 0-2 (ST slope)
        ca,                 # 0-3 (number of major vessels)
        thal_encoded        # 0-3 (thalassemia type)
    ]])

    # WHAT JUST HAPPENED:
    # We created a numpy array with all 13 values in the correct order.
    # This is what the model expects:
    #
    # input_data = [[45, 1, 0, 120, 200, 0, 0, 150, 0, 1.0, 0, 0, 0]]
    #
    # Each number corresponds to a health metric the user entered.
    # The double brackets [[ ]] mean "one patient with these values".
    # --------------------------------------------------------------------


    # --- MAKE THE PREDICTION ---
    # This is where the magic happens!
    # We send the input data to the trained model and get a prediction.
    
    prediction = model.predict(input_data)
    # prediction will be either 0 (no disease) or 1 (has disease)
    
    probability = model.predict_proba(input_data)
    # probability gives us the confidence percentages
    # e.g., [[0.22, 0.78]] means 22% chance no disease, 78% chance disease
    
    # WHAT JUST HAPPENED:
    # The model processed our 13 input values using its learned patterns.
    #
    # Example:
    #   Input: [45, 1, 0, 120, 200, 0, 0, 150, 0, 1.0, 0, 0, 0]
    #   
    #   Model thinks:
    #     - Age 45 is moderate (neutral)
    #     - Male gender (+some risk)
    #     - No chest pain (-risk)
    #     - BP 120 is normal (-risk)
    #     - Cholesterol 200 is normal (-risk)
    #     ...
    #   
    #   Final prediction: 0 (no disease)
    #   Confidence: 78% healthy, 22% disease
    # --------------------------------------------------------------------


    # --- DISPLAY THE RESULT ---
    # We show the prediction to the user with nice formatting.
    
    st.markdown("---")  # Horizontal line separator
    
    # Get the probability of having disease (index 1)
    disease_probability = probability[0][1] * 100  # Convert to percentage
    
    if prediction[0] == 1:
        # Model predicted: HAS DISEASE
        st.error(f"Heart Disease Detected")
        st.write(f"**Risk Probability: {disease_probability:.1f}%**")
        st.write("Please consult a doctor immediately.")
    else:
        # Model predicted: NO DISEASE
        st.success(f"No Heart Disease Detected")
        st.write(f"**Confidence: {(100 - disease_probability):.1f}%**")
        st.write("Keep maintaining a healthy lifestyle!")

    # WHAT JUST HAPPENED:
    # We displayed the result to the user:
    #
    # If disease detected:
    #   ┌─────────────────────────────────┐
    #   │  [RED BOX]                       │
    #   │  Heart Disease Detected          │
    #   │  Risk Probability: 78.0%         │
    #   │  Please consult a doctor.        │
    #   └─────────────────────────────────┘
    #
    # If no disease:
    #   ┌─────────────────────────────────┐
    #   │  [GREEN BOX]                     │
    #   │  No Heart Disease Detected       │
    #   │  Confidence: 85.0%              │
    #   │  Keep maintaining a healthy      │
    #   │  lifestyle!                      │
    #   └─────────────────────────────────┘
    # --------------------------------------------------------------------


# --------------------------------------------------------------------
# STEP 7: ADD INFO SECTION AT THE BOTTOM
# --------------------------------------------------------------------
# This helps users understand what each input means.

st.markdown("---")
st.markdown("### About This App")
st.write("""
This is a machine learning model trained on heart disease data.
**Disclaimer**: This is for educational purposes only. 
Always consult a real doctor for medical advice.

**How it works:**
1. You enter your health data
2. The ML model analyzes it
3. It predicts if you might have heart disease
4. Shows you the result with confidence percentage
""")

# WHAT JUST HAPPENED:
# We added an info section at the bottom of the page.
# It explains:
#   - What the app does
#   - That it's educational only (not real medical advice)
#   - How the prediction works
# --------------------------------------------------------------------


# ====================================================================
# HOW THE ENTIRE FLOW WORKS:
# ====================================================================
#
# 1. User opens app in browser (http://localhost:8501)
#    |
#    v
# 2. Streamlit loads app.py and shows the form
#    |
#    v
# 3. User fills in 13 health fields (age, BP, cholesterol, etc.)
#    |
#    v
# 4. User clicks "Predict" button
#    |
#    v
# 5. app.py converts text inputs to numbers (Male->1, Female->0)
#    |
#    v
# 6. app.py creates numpy array: [45, 1, 0, 120, 200, ...]
#    |
#    v
# 7. app.py calls: model.predict(input_data)
#    |
#    v
# 8. Model processes the data using learned patterns
#    |
#    v
# 9. Model returns: prediction (0 or 1) + probability (0.78)
#    |
#    v
# 10. app.py displays result: "Heart Disease Detected - 78% risk"
#     |
#     v
# 11. User sees the result on the web page
#
# ====================================================================
