from sqlalchemy.orm import Session

from models import PredictionHistory


def save_prediction(
    db: Session,
    data,
    prediction
):
    """
    Save user input and prediction into the database.
    """

    new_prediction = PredictionHistory(

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

        prediction=prediction
    )

    db.add(new_prediction)

    db.commit()

    db.refresh(new_prediction)

    return new_prediction


def get_history(db: Session):
    """
    Return all prediction history.
    """

    return (
        db.query(PredictionHistory)
        .order_by(PredictionHistory.id.desc())
        .all()
    )