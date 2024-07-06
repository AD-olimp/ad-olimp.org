from enum import Enum
from typing import Optional, Union, TypeAlias
from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    field_validator
)


class Grades(str, Enum):
    winner = 'Победитель'
    pre_winner = 'Призер'
    loser = 'Участник'
    

class Step(str, Enum):
    final = 'Заключительный'
    region = 'Региональный'
    qualifying = 'Отборочный'


Point: TypeAlias = Union[float, int]


class OlimpData(BaseModel):
    title:      str                     # Название олимпы
    step:       Step                    # Этап олимпиады
    grade:      list[Grades]            # Диплом участников
    points:     list[Point]             # Баллы участников
    user_class: Optional[list[int]]     # Классы участников
    names:      Optional[list[str]]     # Имена участников
    region:     Optional[list[str]]     # Регион участников
    school:     Optional[list[str]]     # Школы участников
    passing_point: Optional[Point]      # Граничный балл


class OlimpDataList:
    data: list[OlimpData]
    

class OlimpDataFilter(BaseModel):
    year: Optional[list[int]]
    title: Optional[list[str]]
    step: Optional[list[Step]]
    user_class: Optional[list[int]]
    
    
    @field_validator('user_class')
    @classmethod
    def validate_class(cls, user_class):
        """Валидация фильтра на класс. Проверяем, что класс от 1 до 11"""
        
        if user_class not in range(1, 12):
            raise ValidationError(f'Класс пользователя должен быть от 1 до 11, но имеем: {user_class}')
        
        return user_class


class PassingData(BaseModel):
    title:          str           # Название олимпы
    user_class:     Optional[int] # Какой класс писал олимпиаду
    dates:          list[str]     # Даты (лучше строкой)
    passing_points: list[Point]   # Проходные баллы участников


class PassingDataList:
    data: list[PassingData]
    
    
class PassingDataFilter:
    title: Optional[list[str]]
    step: Optional[list[Step]]
    user_class: Optional[list[int]]
