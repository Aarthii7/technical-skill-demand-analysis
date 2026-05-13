from fastapi import FastAPI
import joblib

app = FastAPI()

# Load model and vectorizer
model = joblib.load("models/best_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# Labels
labels = {
    0: "AI_ML",
    1: "Backend",
    2: "Data",
    3: "Frontend",
    4: "Other",
    5: "Security"
}

@app.get("/")
def home():
    return {"message": "Technical Skill Demand Analysis API"}

@app.get("/predict")
def predict(skills: str):

    skills_vector = vectorizer.transform([skills])

    prediction = model.predict(skills_vector)[0]

    return {
        "skills": skills,
        "predicted_category": labels[prediction]
    }