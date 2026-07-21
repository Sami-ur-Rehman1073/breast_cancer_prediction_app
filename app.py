import joblib
import pandas as pd

from fastapi import Depends
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from config import MODEL_PATH
from crud import get_history
from crud import save_prediction
from database import Base
from database import engine
from database import get_db
from schemas import PredictionInput


# =====================================================
# Create Database Tables
# =====================================================

Base.metadata.create_all(bind=engine)


# =====================================================
# Load Trained Model
# =====================================================

model = joblib.load(MODEL_PATH)


# =====================================================
# FastAPI App
# =====================================================

app = FastAPI()


# =====================================================
# Templates
# =====================================================

templates = Jinja2Templates(directory="templates")


# =====================================================
# Home Page
# =====================================================

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "prediction": None
        }
    )


# =====================================================
# Prediction
# =====================================================

@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    data: PredictionInput = Depends(PredictionInput.as_form),
    db: Session = Depends(get_db)
):

    # Convert input to DataFrame

    input_df = pd.DataFrame([
        {
            "mean radius": data.radius_mean,
            "mean texture": data.texture_mean,
            "mean perimeter": data.perimeter_mean,
            "mean area": data.area_mean,
            "mean smoothness": data.smoothness_mean,
            "mean compactness": data.compactness_mean,
            "mean concavity": data.concavity_mean,
            "mean concave points": data.concave_points_mean,
            "mean symmetry": data.symmetry_mean,
            "mean fractal dimension": data.fractal_dimension_mean,

            "radius error": data.radius_se,
            "texture error": data.texture_se,
            "perimeter error": data.perimeter_se,
            "area error": data.area_se,
            "smoothness error": data.smoothness_se,
            "compactness error": data.compactness_se,
            "concavity error": data.concavity_se,
            "concave points error": data.concave_points_se,
            "symmetry error": data.symmetry_se,
            "fractal dimension error": data.fractal_dimension_se,

            "worst radius": data.radius_worst,
            "worst texture": data.texture_worst,
            "worst perimeter": data.perimeter_worst,
            "worst area": data.area_worst,
            "worst smoothness": data.smoothness_worst,
            "worst compactness": data.compactness_worst,
            "worst concavity": data.concavity_worst,
            "worst concave points": data.concave_points_worst,
            "worst symmetry": data.symmetry_worst,
            "worst fractal dimension": data.fractal_dimension_worst,
        }
        ])

    # Prediction

    prediction = model.predict(input_df)[0]

    if prediction == 0:
        prediction_result = "Malignant"
    else:
        prediction_result = "Benign"

    # Save prediction

    save_prediction(
        db=db,
        data=data,
        prediction=prediction_result
    )

    # Return HTML

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "prediction": prediction_result
        }
    )


# =====================================================
# Prediction History
# =====================================================

@app.get("/history", response_class=HTMLResponse)
def history(
    request: Request,
    db: Session = Depends(get_db)
):

    records = get_history(db)

    return templates.TemplateResponse(
        request=request,
        name="history.html",
        context={
            "history": records
        }
    )