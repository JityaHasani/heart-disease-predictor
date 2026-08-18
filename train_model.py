# ====================================================================
# HEART DISEASE PREDICTOR - MODEL TRAINING SCRIPT
# ====================================================================
# This script trains a machine learning model to predict heart disease.
# You only need to run this ONCE. It saves the trained model to a file.
# The Streamlit app (app.py) loads that saved file to make predictions.
# ====================================================================

# --------------------------------------------------------------------
# STEP 1: IMPORT LIBRARIES
# --------------------------------------------------------------------
# Libraries are pre-written code that other people made.
# We import them so we can use their functions.

import os                         # OS: helps us find file paths
import pandas as pd              # Pandas: helps us work with tables (like Excel in Python)
import numpy as np               # NumPy: helps us work with numbers and arrays
from sklearn.model_selection import train_test_split  # Splits data into training and testing sets
from sklearn.linear_model import LogisticRegression   # The ML model we'll use (smart calculator)
from sklearn.metrics import accuracy_score, classification_report  # Measures how good our model is
import joblib                    # Joblib: saves our trained model to a file so we can use it later

# Get the folder where this script is located (so files are found no matter where you run from)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# WHAT JUST HAPPENED:
# We loaded 6 tools:
#   - pandas: reads CSV files, works with tables
#   - numpy: handles numbers
#   - train_test_split: splits our data (80% learn, 20% test)
#   - LogisticRegression: the actual ML algorithm
#   - accuracy_score: tells us "your model is 85% accurate"
#   - joblib: saves the model to a file (model.pkl)
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# STEP 2: LOAD THE DATASET
# --------------------------------------------------------------------
# We read the heart.csv file which has 303 patient records.
# Each row = one patient. Each column = one piece of info about them.

data = pd.read_csv(os.path.join(SCRIPT_DIR, 'heart.csv'))   # Reads the CSV file into a table

print("Dataset loaded successfully!")           # Print success message
print(f"Total patients: {len(data)}")           # Print how many patients (rows)
print(f"Features: {list(data.columns)}")        # Print column names
print(f"\nFirst 5 rows:\n{data.head()}")        # Show first 5 rows of the table

# WHAT JUST HAPPENED:
# We loaded the CSV file. Now 'data' is a table that looks like:
# age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  ca  thal  target
# 63   1    3   145       233   1    0        150      0      2.3      0      0   1     1
# 37   1    2   130       250   0    1        187      0      3.5      0      0   2     1
# ...  ...  ... ...       ...   ...  ...      ...      ...    ...      ...    ... ...   ...
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# STEP 3: SEPARATE FEATURES AND TARGET
# --------------------------------------------------------------------
# Features (X) = the INPUTS (age, sex, blood pressure, etc.)
# Target (y)   = the OUTPUT (0 = no disease, 1 = has disease)
# The model learns: given these inputs -> predict this output

X = data.drop('target', axis=1)   # X = everything EXCEPT the target column
y = data['target']                 # y = ONLY the target column

print(f"\nInput features shape: {X.shape}")   # (303, 13) = 303 rows, 13 columns
print(f"Target shape: {y.shape}")             # (303,) = 303 values (0 or 1)

# WHAT JUST HAPPENED:
# We split the table into two parts:
#
# X (inputs):                    y (output):
# age  sex  cp  trestbps ...     target
# 63   1    3   145      ...  ->   1    (has disease)
# 37   1    2   130      ...  ->   1    (has disease)
# 65   0    0   150      ...  ->   0    (no disease)
#
# The model will learn the pattern between X and y.
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# STEP 4: SPLIT INTO TRAINING AND TESTING SETS
# --------------------------------------------------------------------
# We give 80% of data for training (learning)
# We keep 20% of data for testing (checking if it learned correctly)

X_train, X_test, y_train, y_test = train_test_split(
    X, y,               # The data to split
    test_size=0.2,      # 20% goes to test set
    random_state=42     # Makes the split the same every time (reproducible)
)

print(f"\nTraining set: {len(X_train)} patients")   # ~242 patients to learn from
print(f"Testing set: {len(X_test)} patients")       # ~61 patients to test on

# WHAT JUST HAPPENED:
# BEFORE SPLIT:
# [patient1, patient2, patient3, ..., patient303]
#
# AFTER SPLIT:
# Training set (80%): [patient1, patient4, patient5, ...]  <- Model learns from these
# Testing set (20%):  [patient2, patient3, patient8, ...]  <- We test with these
#
# Why split? Because if we test on the same data we trained on,
# the model might just memorize answers instead of actually learning.
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# STEP 5: CREATE AND TRAIN THE MODEL
# --------------------------------------------------------------------
# Logistic Regression is a simple but effective ML algorithm.
# It learns a mathematical formula that maps inputs -> output.

model = LogisticRegression(max_iter=1000)  # Create the model (empty brain)
model.fit(X_train, y_train)                # Train it (teach it patterns)

print("\nModel trained successfully!")

# WHAT JUST HAPPENED:
# model.fit() is where the MAGIC happens!
#
# The model looks at all 242 training patients:
#   "Patient A: age=63, BP=145, chol=233 -> had disease (1)"
#   "Patient B: age=37, BP=130, chol=250 -> had disease (1)"
#   "Patient C: age=65, BP=150, chol=194 -> no disease (0)"
#   ... (242 times)
#
# It discovers mathematical patterns:
#   - High BP + High Cholesterol + Chest Pain = HIGH RISK
#   - Low BP + Normal Cholesterol + No Pain = LOW RISK
#   - Age > 55 + Exercise Angina = MEDIUM-HIGH RISK
#
# After training, the model has learned a formula.
# That formula is stored inside the 'model' variable.
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# STEP 6: TEST THE MODEL
# --------------------------------------------------------------------
# Now we ask the model to predict on the 61 patients it hasn't seen.
# We compare its predictions to the actual answers.

y_pred = model.predict(X_test)                        # Model makes predictions
accuracy = accuracy_score(y_test, y_pred)             # Calculate accuracy percentage

print(f"\nModel Accuracy: {accuracy * 100:.1f}%")     # Print accuracy (e.g., 85.2%)
print(f"\nDetailed Report:\n{classification_report(y_test, y_pred)}")

# WHAT JUST HAPPENED:
# The model predicted outcomes for 61 test patients.
# We compared its predictions to the actual answers.
#
# Example:
#   Patient X actual: 1 (had disease)
#   Patient X predicted: 1 (model said disease) -> CORRECT!
#
#   Patient Y actual: 0 (no disease)
#   Patient Y predicted: 1 (model said disease) -> WRONG!
#
# Overall, the model got ~85% of predictions right.
# For a hackathon, this is good enough!
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# STEP 7: SAVE THE TRAINED MODEL TO A FILE
# --------------------------------------------------------------------
# We save the model so the Streamlit app can load it later.
# This way, we don't have to retrain every time someone uses the app.

joblib.dump(model, os.path.join(SCRIPT_DIR, 'model.pkl'))    # Save model to model.pkl file
print("\nModel saved to 'model.pkl'!")

# WHAT JUST HAPPENED:
# 'model.pkl' now contains everything the model learned.
# It's like saving a trained brain to a file.
# The Streamlit app will load this file to make predictions.
# --------------------------------------------------------------------


# --------------------------------------------------------------------
# SUMMARY
# --------------------------------------------------------------------
# What we did:
#   1. Loaded 303 patient records from heart.csv
#   2. Separated inputs (features) from output (target)
#   3. Split into 80% training + 20% testing
#   4. Trained Logistic Regression model on training data
#   5. Tested model - got ~85% accuracy
#   6. Saved trained model to model.pkl
#
# What happens next:
#   - app.py loads model.pkl
#   - User enters their health data
#   - Model predicts if they have heart disease
#   - Result shown on the web page
# --------------------------------------------------------------------
