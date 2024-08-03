import datetime
from typing import Optional
from pydantic import BaseModel, Field, conint

from src.models.common import OlympTitle, Step, Grades


class DataFilter(BaseModel):
    years: Optional[list[conint(gt=2000)]] = Field(default=datetime.datetime.now().year)
    user_class: Optional[list[conint(gt=0, lt=12)]] = Field(default=[9, 10, 11])
    title: Optional[list[OlympTitle]]
    step: Optional[list[Step]]


class OlympData(BaseModel):
    title: OlympTitle                      # Название олимпы
    step: Step                             # Этап олимпиады
    grade: list[Grades]                    # Диплом участников
    points: list[float]                    # Баллы участников
    user_class: Optional[list[int]]        # Классы участников
    names: Optional[list[str]]             # Имена участников
    region: Optional[list[str]]            # Регион участников
    school: Optional[list[str]]            # Школы участников
    passing_point: Optional[list[float]]   # Проходной балл
    boundary_point: Optional[list[float]]  # Граничный балл


class PassingData(BaseModel):
    title: OlympTitle            # Название олимпы
    passing_points: list[float]  # Проходные баллы участников
    years: list[str]             # Даты (лучше строкой)
    user_class: list[int]        # Какой класс писал олимпиаду


class PassingDataFilter:
    title: Optional[list[OlympTitle]]
    year: Optional[list[int]] = Field(default=datetime.datetime.now().year)
    user_class: Optional[list[int]] = Field(default=[9, 10, 11])


class BoundaryData(BaseModel):
    title: OlympTitle                        # Название олимпы
    winner_boundary_points: list[float]      # Граничные баллы на победителя
    pre_winner_boundary_points: list[float]  # Проходные баллы участников
    years: list[str]                         # Даты (лучше строкой)
    user_class: list[int]                    # Какой класс писал олимпиаду

