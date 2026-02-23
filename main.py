from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Student Academic Risk Prediction API")

# -----------------------------
# Load Model & Feature Order
# -----------------------------
pipeline = joblib.load("academic_risk_pipeline.pkl")
MODEL_FEATURES = joblib.load("pipeline_features.pkl")

print("✅ Pipeline Loaded Successfully")
print("📌 Expected Features:", MODEL_FEATURES)


# -----------------------------
# Request Schema
# -----------------------------
class StudentData(BaseModel):
    data: dict


# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
def home():
    return {
        "message": "Student Risk Management API is running 🚀"
    }


# -----------------------------
# Prediction Endpoint
# -----------------------------
@app.post("/predict")
def predict(student: StudentData):
    try:
        input_dict = student.data

        # Create empty dataframe with all required features
        df = pd.DataFrame(columns=MODEL_FEATURES)
        df.loc[0] = 0  # initialize all values as 0

        # Fill only provided fields
        for key, value in input_dict.items():
            if key in MODEL_FEATURES:
                df.at[0, key] = value

        # Make prediction
        prediction = pipeline.predict(df)[0]
        probability = float(pipeline.predict_proba(df)[0][1])

        # Risk level classification
        if probability < 0.3:
            risk_level = "Low"
        elif probability < 0.6:
            risk_level = "Medium"
        else:
            risk_level = "High"

        return {
            "prediction": int(prediction),
            "risk_level": risk_level,
            "risk_probability": round(probability, 3)
        }

    except Exception as e:
        return {"error": str(e)}