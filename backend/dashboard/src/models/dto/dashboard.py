import datetime
from typing import Optional
from pydantic import BaseModel, Field, conint

from src.models.common import OlympTitle, Step, Grades


class DataFilter(BaseModel):
    year: Optional[list[conint(gt=2000)]] = Field(default=[datetime.datetime.now().year, ])
    user_class: Optional[list[conint(gt=0, lt=12)]] = Field(default=[9, 10, 11])
    title: Optional[list[OlympTitle]]
    step: Optional[list[Step]]


class OlympData(BaseModel):
    title: OlympTitle                # Название олимпы                             # Этап олимпиады
    grade: Grades                    # Диплом участников
    points: float                    # Баллы участников
    year: int                        # Год проведения
    user_class: Optional[int]        # Классы участников
    names: Optional[str]             # Имена участников
    region: Optional[str]            # Регион участников
    school: Optional[str]            # Школы участников


class PassingData(BaseModel):
    passing_points: float        # Проходные баллы участников
    years: int                   # Даты (лучше строкой, но Олегу было удобнее интом)
    title: OlympTitle            # Название олимпы
    user_class: int              # Какой класс писал олимпиаду


class BoundaryData(BaseModel):
    winner_boundary_points: float      # Граничные баллы на победителя
    pre_winner_boundary_points: float  # Проходные баллы участников
    years: int                         # Даты (лучше строкой)
    title: OlympTitle                  # Название олимпы
    user_class: int                    # Какой класс писал олимпиаду

