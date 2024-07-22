import datetime
from enum import Enum
from typing import Optional, Union, TypeAlias
from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    field_validator
)

from src.models.common import OlympTitles, Step, Grades


class OlympData(BaseModel):
    title: OlympTitles  # Название олимпы
    step: Step  # Этап олимпиады
    grade: list[Grades]  # Диплом участников
    points: list[float]  # Баллы участников
    user_class: Optional[list[int]]  # Классы участников
    names: Optional[list[str]]  # Имена участников
    region: Optional[list[str]]  # Регион участников
    school: Optional[list[str]]  # Школы участников
    passing_point: Optional[float]  # Граничный балл


class OlympDataList:
    data: list[OlympData]


class OlympDataFilter(BaseModel):
    year: Optional[list[int]] = Field(default=datetime.datetime.now().year)
    user_class: Optional[list[int]] = Field(default=[9, 10, 11])
    title: Optional[list[OlympTitles]]
    step: Optional[list[Step]]

    @classmethod
    @field_validator('user_class')
    def validate_class(cls, user_class):
        """Валидация фильтра на класс. Проверяем, что класс от 1 до 11"""

        if user_class not in range(1, 12):
            raise ValidationError(f'Класс пользователя должен быть от 1 до 11, но имеем: {user_class}')

        return user_class


class PassingData(BaseModel):
    title: OlympTitles           # Название олимпы
    user_class: Optional[int]    # Какой класс писал олимпиаду
    date_start: str              # Даты (лучше строкой)
    date_end: str              # Даты (лучше строкой)
    passing_points: list[float]  # Проходные баллы участников


class PassingDataList:
    data: list[PassingData]


class PassingDataFilter:
    title: Optional[list[str]]
    step: Optional[list[Step]]
    user_class: Optional[list[int]]