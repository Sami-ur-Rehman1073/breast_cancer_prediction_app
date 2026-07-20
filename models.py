from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime
from datetime import datetime

from database import Base


class PredictionHistory(Base):
    __tablename__ = "prediction_history"

    id = Column(Integer, primary_key=True, index=True)

    radius_mean = Column(Float)
    texture_mean = Column(Float)
    perimeter_mean = Column(Float)
    area_mean = Column(Float)
    smoothness_mean = Column(Float)
    compactness_mean = Column(Float)
    concavity_mean = Column(Float)
    concave_points_mean = Column(Float)
    symmetry_mean = Column(Float)
    fractal_dimension_mean = Column(Float)

    prediction = Column(String(20))

    created_at = Column(DateTime, default=datetime.utcnow)