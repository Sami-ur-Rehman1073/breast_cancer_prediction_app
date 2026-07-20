from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime

from database import Base


class PredictionHistory(Base):
    __tablename__ = "prediction_history"

    # ==========================
    # Primary Key
    # ==========================

    id = Column(Integer, primary_key=True, index=True)

    # ==========================
    # Mean Features
    # ==========================

    radius_mean = Column(Float, nullable=False)
    texture_mean = Column(Float, nullable=False)
    perimeter_mean = Column(Float, nullable=False)
    area_mean = Column(Float, nullable=False)
    smoothness_mean = Column(Float, nullable=False)
    compactness_mean = Column(Float, nullable=False)
    concavity_mean = Column(Float, nullable=False)
    concave_points_mean = Column(Float, nullable=False)
    symmetry_mean = Column(Float, nullable=False)
    fractal_dimension_mean = Column(Float, nullable=False)

    # ==========================
    # Standard Error Features
    # ==========================

    radius_se = Column(Float, nullable=False)
    texture_se = Column(Float, nullable=False)
    perimeter_se = Column(Float, nullable=False)
    area_se = Column(Float, nullable=False)
    smoothness_se = Column(Float, nullable=False)
    compactness_se = Column(Float, nullable=False)
    concavity_se = Column(Float, nullable=False)
    concave_points_se = Column(Float, nullable=False)
    symmetry_se = Column(Float, nullable=False)
    fractal_dimension_se = Column(Float, nullable=False)

    # ==========================
    # Worst Features
    # ==========================

    radius_worst = Column(Float, nullable=False)
    texture_worst = Column(Float, nullable=False)
    perimeter_worst = Column(Float, nullable=False)
    area_worst = Column(Float, nullable=False)
    smoothness_worst = Column(Float, nullable=False)
    compactness_worst = Column(Float, nullable=False)
    concavity_worst = Column(Float, nullable=False)
    concave_points_worst = Column(Float, nullable=False)
    symmetry_worst = Column(Float, nullable=False)
    fractal_dimension_worst = Column(Float, nullable=False)

    # ==========================
    # Prediction
    # ==========================

    prediction = Column(String(20), nullable=False)

    # ==========================
    # Timestamp
    # ==========================

    created_at = Column(DateTime, default=datetime.utcnow)