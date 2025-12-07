import pandas as pd
import joblib
from db_connect import get_connection
from sklearn.preprocessing import LabelEncoder

conn = get_connection()

# Load model
model = joblib.load("model.pkl")

# Load Data
df = pd.read_sql("SELECT * FROM customers", conn)

# Encode gender
df['gender'] = df['gender'].astype(str)
le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])

# Features
X = df[['age', 'gender', 'tenure_months', 'monthly_charges', 'total_charges']]

# Predictions
df['predicted_churn'] = model.predict(X)

# Save predictions into DB
cursor = conn.cursor()

for index, row in df.iterrows():
    cursor.execute("""
        UPDATE customers
        SET predicted_churn = %s
        WHERE customer_id = %s
    """, (bool(row['predicted_churn']), int(row['customer_id'])))

conn.commit()
cursor.close()
conn.close()

print("Predictions saved to database successfully!")
