# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

print("Starting model training process...")

# --- 1. Load Data ---
df = pd.read_csv('data/dataset.csv')

# --- 2. Prepare Data ---
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
symptoms = X.columns.tolist()

# --- 3. Train Model ---
model = RandomForestClassifier(random_state=42)
model.fit(X, y)
print("Model training completed successfully.")

# --- 4. Save Model and Symptoms List ---
os.makedirs('models', exist_ok=True)
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('models/symptoms.pkl', 'wb') as f:
    pickle.dump(symptoms, f)

print("✅ Model and symptoms list have been saved to the 'models' folder.")