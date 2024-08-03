from typing import Optional

from pydantic import BaseModel

from src.models.common import OlympTitle, Grades


class UpdateOlympDataScheme(BaseModel):
    title: OlympTitle
    grade: Grades
    points: float
    year: int
    user_class: Optional[int]
    names: Optional[str]
    region: Optional[str]
    school: Optional[str]


class UpdatePassingDataScheme(BaseModel):
    passing_points: float
    years: str
    title: OlympTitle
    user_class: Optional[int]


class UpdateBoundaryDataScheme(BaseModel):
    winner_boundary_points: float
    pre_winner_boundary_points: float
    years: int
    title: OlympTitle
    user_class: Optional[int]
