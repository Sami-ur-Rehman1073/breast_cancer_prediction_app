from typing import Annotated

from fastapi import Form
from pydantic import BaseModel


class PredictionInput(BaseModel):

    # ==========================
    # Mean Features
    # ==========================

    radius_mean: float
    texture_mean: float
    perimeter_mean: float
    area_mean: float
    smoothness_mean: float
    compactness_mean: float
    concavity_mean: float
    concave_points_mean: float
    symmetry_mean: float
    fractal_dimension_mean: float

    # ==========================
    # Standard Error Features
    # ==========================

    radius_se: float
    texture_se: float
    perimeter_se: float
    area_se: float
    smoothness_se: float
    compactness_se: float
    concavity_se: float
    concave_points_se: float
    symmetry_se: float
    fractal_dimension_se: float

    # ==========================
    # Worst Features
    # ==========================

    radius_worst: float
    texture_worst: float
    perimeter_worst: float
    area_worst: float
    smoothness_worst: float
    compactness_worst: float
    concavity_worst: float
    concave_points_worst: float
    symmetry_worst: float
    fractal_dimension_worst: float

    @classmethod
    def as_form(
        cls,
        radius_mean: Annotated[float, Form(...)],
        texture_mean: Annotated[float, Form(...)],
        perimeter_mean: Annotated[float, Form(...)],
        area_mean: Annotated[float, Form(...)],
        smoothness_mean: Annotated[float, Form(...)],
        compactness_mean: Annotated[float, Form(...)],
        concavity_mean: Annotated[float, Form(...)],
        concave_points_mean: Annotated[float, Form(...)],
        symmetry_mean: Annotated[float, Form(...)],
        fractal_dimension_mean: Annotated[float, Form(...)],
        radius_se: Annotated[float, Form(...)],
        texture_se: Annotated[float, Form(...)],
        perimeter_se: Annotated[float, Form(...)],
        area_se: Annotated[float, Form(...)],
        smoothness_se: Annotated[float, Form(...)],
        compactness_se: Annotated[float, Form(...)],
        concavity_se: Annotated[float, Form(...)],
        concave_points_se: Annotated[float, Form(...)],
        symmetry_se: Annotated[float, Form(...)],
        fractal_dimension_se: Annotated[float, Form(...)],
        radius_worst: Annotated[float, Form(...)],
        texture_worst: Annotated[float, Form(...)],
        perimeter_worst: Annotated[float, Form(...)],
        area_worst: Annotated[float, Form(...)],
        smoothness_worst: Annotated[float, Form(...)],
        compactness_worst: Annotated[float, Form(...)],
        concavity_worst: Annotated[float, Form(...)],
        concave_points_worst: Annotated[float, Form(...)],
        symmetry_worst: Annotated[float, Form(...)],
        fractal_dimension_worst: Annotated[float, Form(...)]
    ):
        return cls(
            radius_mean=radius_mean,
            texture_mean=texture_mean,
            perimeter_mean=perimeter_mean,
            area_mean=area_mean,
            smoothness_mean=smoothness_mean,
            compactness_mean=compactness_mean,
            concavity_mean=concavity_mean,
            concave_points_mean=concave_points_mean,
            symmetry_mean=symmetry_mean,
            fractal_dimension_mean=fractal_dimension_mean,
            radius_se=radius_se,
            texture_se=texture_se,
            perimeter_se=perimeter_se,
            area_se=area_se,
            smoothness_se=smoothness_se,
            compactness_se=compactness_se,
            concavity_se=concavity_se,
            concave_points_se=concave_points_se,
            symmetry_se=symmetry_se,
            fractal_dimension_se=fractal_dimension_se,
            radius_worst=radius_worst,
            texture_worst=texture_worst,
            perimeter_worst=perimeter_worst,
            area_worst=area_worst,
            smoothness_worst=smoothness_worst,
            compactness_worst=compactness_worst,
            concavity_worst=concavity_worst,
            concave_points_worst=concave_points_worst,
            symmetry_worst=symmetry_worst,
            fractal_dimension_worst=fractal_dimension_worst,
        )