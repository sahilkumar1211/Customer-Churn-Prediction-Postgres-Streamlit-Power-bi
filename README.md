Customer Churn Prediction using PostgreSQL + Streamlit + Power BI

This project predicts customer churn using a Machine Learning model, stores predictions in PostgreSQL, displays results in a Streamlit app, and visualizes real-time data in Power BI (DirectQuery Mode).
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Tech Stack:

Python
PostgreSQL
Streamlit
Power BI
Scikit-Learn (Random Forest Classifier)
Pandas
SQLAlchemy / Psycopg2
Psycopg2
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📂 Project Structure:
├── src/
│   ├── app.py                  # Streamlit UI for real-time churn prediction
│   ├── db_connect.py           # PostgreSQL connection file
│   ├── model_train.py          # ML model training + saving predictions
│   ├── store_predictions.py    # Update predicted churn column in DB
│   ├── sql/
│   │   ├── create_table.sql
│   │   ├── sample_insert.sql
├── requirements.txt
└── README.md
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🛢️ Database Schema (customers table):
ColumnName	       Type	          Description
customer_id  	     Integer(PK)	    Unique ID
name	             Text           	Customer name
age	               Integer	        Age
gender	           Text	          Male/Female
tenure_months	     Integer	        Subscription months
monthly_charges    Float	          Monthly fee
total_charges	     Float	          Total spent
churn	             Boolean	        Actual churn
predicted_churn    Boolean	        ML model result

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🤖 Machine Learning Model

Algorithm → Random Forest Classifier

Features used:
age
gender
tenure_months
monthly_charges
total_charges
Model predicts:  Will the customer churn or not?
Predictions are then saved into PostgreSQL.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🖥️ Streamlit App

Run using:

python app.py

Features:

Takes customer details as input

Predicts churn in real-time

Displays result immediately
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
📊 Power BI Dashboard (DirectQuery Mode)

Connected PostgreSQL using DirectQuery

Visualizes:

Predicted vs Actual churn (Pie Chart)

Charges analysis (Bar Chart)

Customer demographics

Auto-refresh when database changes

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚙️ Setup Instructions
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Create PostgreSQL Tables
-- Run from create_table.sql

3️⃣ Insert Sample Data
-- Run from sample_insert.sql

4️⃣ Train Model
python model_train.py

5️⃣ Save Predictions Back to DB
python store_predictions.py

6️⃣ Run Streamlit App
python app.py

📬 Author

Sahil Kumar (@sahilkumar1211)
Data Science & ML Projects
--------------------------------------------------------------------------------------------------------------










