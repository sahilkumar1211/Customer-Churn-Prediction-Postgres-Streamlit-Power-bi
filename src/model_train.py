import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
from db_connect import get_connection

# Connect to Database
conn = get_connection()

# Load Data
df = pd.read_sql("SELECT * FROM customers", conn)

# Encode gender (Male/Female → 0/1)
df['gender'] = df['gender'].astype(str)
le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])

# Features and Target
X = df[['age', 'gender', 'tenure_months', 'monthly_charges', 'total_charges']]
y = df['churn']

# Train Model
model = RandomForestClassifier()
model.fit(X, y)

# Save Model
joblib.dump(model, "model.pkl")

print("Model training complete. File saved as model.pkl")

conn.close()
