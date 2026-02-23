# 🎓 Student Academic Risk Prediction System

## 🚀 Project Overview

The Student Academic Risk Prediction System is a Machine Learning-based backend application that predicts whether a student is at academic risk based on demographic, academic, and behavioral factors.

This system uses a trained Random Forest model integrated with a FastAPI backend to provide real-time predictions through a REST API.

The goal of this project is to help educational institutions identify at-risk students early and enable timely academic intervention.

---

# 🧠 Problem Statement

Many students struggle academically due to multiple factors such as:

- Low study time
- High absenteeism
- Past academic failures
- Poor grades (G1, G2)
- Family and social factors
- Alcohol consumption
- Lack of support systems

It is difficult to manually identify at-risk students early.  
This project builds a Machine Learning system to automate that process.

---

# 📊 Dataset Used

The model was trained on the Student Performance dataset containing:

- Demographic features (age, family education, guardian, etc.)
- Academic features (G1, G2, studytime, failures)
- Social behavior (goout, Dalc, Walc)
- Support features (schoolsup, famsup, internet, higher education intent)
- Engineered features:
  - total_alcohol
  - academic_effort
  - support_score

Total features used: **43**

---

# 🔬 Machine Learning Pipeline

## 1️⃣ Data Preprocessing

- Handled categorical variables using one-hot encoding
- Engineered new features
- Standardized numeric features using `StandardScaler`

---

## 2️⃣ Model Selection

We used:

- `RandomForestClassifier`

Why Random Forest?

- Handles nonlinear relationships well
- Works well with mixed feature types
- Robust to noise
- Good performance without heavy tuning

---

## 3️⃣ Pipeline Creation

We built a Scikit-Learn Pipeline:

- StandardScaler
- RandomForestClassifier

Then we saved:

- `academic_risk_pipeline.pkl`
- `pipeline_features.pkl`

This ensures:
- Correct feature order
- No mismatch during prediction
- Easy backend integration

---

# ⚙️ Backend Development (FastAPI)

We built a REST API using FastAPI.

## 🏗 Backend Structure

- Load trained pipeline
- Load correct feature order
- Accept student data as JSON
- Convert input to DataFrame
- Fill missing features with default value (0)
- Reorder columns
- Generate prediction
- Return risk probability and risk level

---

# 📡 API Endpoints

## GET /

Returns API status.

Response:
```json
{
  "message": "Student Risk Management API is running 🚀"
}
```

---

## POST /predict

Accepts student data and returns prediction.

Request format:

```json
{
  "data": {
    "age": 17,
    "studytime": 1,
    "failures": 2,
    "absences": 15,
    "G1": 8,
    "G2": 7
  }
}
```

Response format:

```json
{
  "prediction": 1,
  "risk_level": "High",
  "risk_probability": 0.742
}
```

---

# 🎯 Risk Classification Logic

Instead of using only the model’s 0.5 threshold, we created practical risk levels:

| Probability | Risk Level |
|-------------|------------|
| < 0.3       | Low Risk   |
| 0.3–0.6     | Medium Risk|
| > 0.6       | High Risk  |

This makes the system more realistic for educational monitoring.

---

# 🧪 Example Output

```json
{
  "prediction": 0,
  "risk_level": "Medium",
  "risk_probability": 0.4
}
```

Explanation:

- Probability = 0.4
- Below 0.5 → Not high-risk by model threshold
- But between 0.3–0.6 → Medium Risk category

---

# 🛠 Technologies Used

- Python
- Scikit-learn
- Pandas
- FastAPI
- Uvicorn
- Joblib

---

# 📂 Project Structure

```
Backend-SRM/
│
├── main.py
├── academic_risk_pipeline.pkl
├── pipeline_features.pkl
├── requirements.txt
└── README.md
```

---

# ▶️ How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn scikit-learn pandas joblib
```

---

### 2️⃣ Run the server

```bash
python -m uvicorn main:app --reload
```

---

### 3️⃣ Open Swagger UI

```
http://127.0.0.1:8000/docs
```

You can test the `/predict` endpoint directly.

---

# 🔥 What We Built From Scratch

✅ Data preprocessing  
✅ Feature engineering  
✅ Model training  
✅ Scikit-learn pipeline  
✅ Model persistence  
✅ Backend API  
✅ Risk classification system  
✅ Error handling  
✅ Professional response format  

This is a complete ML + Backend integration project.

---

# 🚀 Future Improvements

- Add MongoDB to store predictions
- Add frontend (React / HTML)
- Add model explainability (Feature Importance)
- Deploy on Render or Railway
- Add authentication system

---

# 💼 Why This Project Is Strong

This project demonstrates:

- Machine Learning knowledge
- Backend development skills
- API development
- Model deployment understanding
- Production-level thinking

It is suitable for:

- Academic submission
- Hackathons
- Resume / Portfolio
- Placement interviews

---

# 👨‍💻 Author

Neeraj Mittal  
Student Risk Management ML Project

---

# ⭐ Conclusion

This project successfully integrates a trained Machine Learning model with a production-ready FastAPI backend to predict academic risk in real-time.

It transforms raw student data into actionable academic insights.
