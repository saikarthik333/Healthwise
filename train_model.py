<<<<<<< HEAD
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

print("Starting model training process...")

df = pd.read_csv('data/dataset.csv')

X = df.iloc[:, :-1]
y = df.iloc[:, -1]
symptoms = X.columns.tolist()

model = RandomForestClassifier(random_state=42)
model.fit(X, y)
print("Model training completed successfully.")

os.makedirs('models', exist_ok=True)
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('models/symptoms.pkl', 'wb') as f:
    pickle.dump(symptoms, f)


print("✅ Model and symptoms list have been saved to the 'models' folder.")
=======
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

print("Starting model training process...")

df = pd.read_csv('data/dataset.csv')

X = df.iloc[:, :-1]
y = df.iloc[:, -1]
symptoms = X.columns.tolist()

model = RandomForestClassifier(random_state=42)
model.fit(X, y)
print("Model training completed successfully.")

os.makedirs('models', exist_ok=True)
with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('models/symptoms.pkl', 'wb') as f:
    pickle.dump(symptoms, f)


print("✅ Model and symptoms list have been saved to the 'models' folder.")
>>>>>>> 1a0a8cc8fb36b307e53c0b9a4508420478a4b269
