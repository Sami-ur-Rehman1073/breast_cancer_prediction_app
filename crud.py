from sqlalchemy.orm import Session

from models import PredictionHistory
from schemas import PredictionInput


def save_prediction(
    db: Session,
    data: PredictionInput,
    prediction: str
):
    """
    Save the user input and prediction into the database.
    """

    prediction_record = PredictionHistory(

        # ==========================
        # Mean Features
        # ==========================

        radius_mean=data.radius_mean,
        texture_mean=data.texture_mean,
        perimeter_mean=data.perimeter_mean,
        area_mean=data.area_mean,
        smoothness_mean=data.smoothness_mean,
        compactness_mean=data.compactness_mean,
        concavity_mean=data.concavity_mean,
        concave_points_mean=data.concave_points_mean,
        symmetry_mean=data.symmetry_mean,
        fractal_dimension_mean=data.fractal_dimension_mean,

        # ==========================
        # Standard Error Features
        # ==========================

        radius_se=data.radius_se,
        texture_se=data.texture_se,
        perimeter_se=data.perimeter_se,
        area_se=data.area_se,
        smoothness_se=data.smoothness_se,
        compactness_se=data.compactness_se,
        concavity_se=data.concavity_se,
        concave_points_se=data.concave_points_se,
        symmetry_se=data.symmetry_se,
        fractal_dimension_se=data.fractal_dimension_se,

        # ==========================
        # Worst Features
        # ==========================

        radius_worst=data.radius_worst,
        texture_worst=data.texture_worst,
        perimeter_worst=data.perimeter_worst,
        area_worst=data.area_worst,
        smoothness_worst=data.smoothness_worst,
        compactness_worst=data.compactness_worst,
        concavity_worst=data.concavity_worst,
        concave_points_worst=data.concave_points_worst,
        symmetry_worst=data.symmetry_worst,
        fractal_dimension_worst=data.fractal_dimension_worst,

        # ==========================
        # Prediction
        # ==========================

        prediction=prediction
    )

    db.add(prediction_record)

    db.commit()

    db.refresh(prediction_record)

    return prediction_record


def get_history(db: Session):
    """
    Return all prediction records ordered from newest to oldest.
    """

    history = (
        db.query(PredictionHistory)
        .order_by(PredictionHistory.id.desc())
        .all()
    )

    return history