import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os

def train_model():
    df = pd.read_csv('D:\24feb25\Python\Healthwise\data\symptom_Description.csv')

    X = df.drop('Disease', axis=1)
    y = df['Disease']

    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    X.fillna(0, inplace=True)  # Optional: Replace NaNs with 0
    X = X.apply(LabelEncoder().fit_transform)

    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    os.makedirs('saved_models', exist_ok=True)
    joblib.dump(model, 'D:\24feb25\Python\Healthwise\saved_models\model.pkl')
    joblib.dump(le, 'D:\24feb25\Python\Healthwise\saved_models\label_encoder.pkl')

    print("✅ Model and Label Encoder saved!")
