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

# Create Database Tables


Base.metadata.create_all(bind=engine)

# Load Trained Model

model = joblib.load(MODEL_PATH)

# FastAPI App

app = FastAPI()


# Jinja Templates

templates = Jinja2Templates(directory="templates")


# Home Page

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": None
        }
    )


# Predict

@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    data: PredictionInput = Depends(PredictionInput.as_form),
    db: Session = Depends(get_db)
):

    # Convert user input into DataFrame

    input_df = pd.DataFrame(
        [
            {
                "radius_mean": data.radius_mean,
                "texture_mean": data.texture_mean,
                "perimeter_mean": data.perimeter_mean,
                "area_mean": data.area_mean,
                "smoothness_mean": data.smoothness_mean,
                "compactness_mean": data.compactness_mean,
                "concavity_mean": data.concavity_mean,
                "concave_points_mean": data.concave_points_mean,
                "symmetry_mean": data.symmetry_mean,
                "fractal_dimension_mean": data.fractal_dimension_mean,

                "radius_se": data.radius_se,
                "texture_se": data.texture_se,
                "perimeter_se": data.perimeter_se,
                "area_se": data.area_se,
                "smoothness_se": data.smoothness_se,
                "compactness_se": data.compactness_se,
                "concavity_se": data.concavity_se,
                "concave_points_se": data.concave_points_se,
                "symmetry_se": data.symmetry_se,
                "fractal_dimension_se": data.fractal_dimension_se,

                "radius_worst": data.radius_worst,
                "texture_worst": data.texture_worst,
                "perimeter_worst": data.perimeter_worst,
                "area_worst": data.area_worst,
                "smoothness_worst": data.smoothness_worst,
                "compactness_worst": data.compactness_worst,
                "concavity_worst": data.concavity_worst,
                "concave_points_worst": data.concave_points_worst,
                "symmetry_worst": data.symmetry_worst,
                "fractal_dimension_worst": data.fractal_dimension_worst,
            }
        ]
    )

    # Make Prediction

    prediction = model.predict(input_df)[0]

    if prediction == 0:
        prediction_result = "Malignant"
    else:
        prediction_result = "Benign"


   # Save Prediction

    save_prediction(
        db=db,
        data=data,
        prediction=prediction_result
    )

    # Return Result

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": prediction_result
        }
    )


# Prediction History

@app.get("/history", response_class=HTMLResponse)
def history(
    request: Request,
    db: Session = Depends(get_db)
):

    history = get_history(db)

    return templates.TemplateResponse(
        "history.html",
        {
            "request": request,
            "history": history
        }
    )