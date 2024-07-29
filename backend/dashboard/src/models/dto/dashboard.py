import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError, field_validator

from src.models.common import OlympTitle, Step, Grades


class OlympData(BaseModel):
    title: OlympTitle  # Название олимпы
    step: Step  # Этап олимпиады
    grade: list[Grades]  # Диплом участников
    points: list[float]  # Баллы участников
    user_class: Optional[list[int]]  # Классы участников
    names: Optional[list[str]]  # Имена участников
    region: Optional[list[str]]  # Регион участников
    school: Optional[list[str]]  # Школы участников
    passing_point: Optional[float]  # Граничный балл


class OlympDataFilter(BaseModel):
    year: Optional[list[int]] = Field(default=datetime.datetime.now().year)
    user_class: Optional[list[int]] = Field(default=[9, 10, 11])
    title: Optional[list[OlympTitle]]
    step: Optional[list[Step]]

    @classmethod
    @field_validator('user_class')
    def validate_class(cls, user_class):
        """Валидация фильтра на класс. Проверяем, что класс от 1 до 11"""

        if user_class not in range(1, 12):
            raise ValidationError(f'Класс пользователя должен быть от 1 до 11, но имеем: {user_class}')

        return user_class


class PassingData(BaseModel):
    title: OlympTitle            # Название олимпы
    passing_points: list[float]  # Проходные баллы участников
    years: list[str]             # Даты (лучше строкой)
    user_class: list[int]        # Какой класс писал олимпиаду


class BoundaryData(BaseModel):
    title: OlympTitle                        # Название олимпы
    winner_boundary_points: list[float]      # Граничные баллы на победителя
    pre_winner_boundary_points: list[float]  # Проходные баллы участников
    years: list[str]                         # Даты (лучше строкой)
    user_class: list[int]                    # Какой класс писал олимпиаду


class PassingDataFilter:
    titles: Optional[list[str]]
    step: Optional[list[Step]]
    user_class: Optional[list[int]]
