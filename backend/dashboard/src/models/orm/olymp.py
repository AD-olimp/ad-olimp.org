from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseTable
from src.models.common import OlympTitle, Grades


class OlympORM(BaseTable):
    """Данные участников олимпиады"""

    __tablename__ = 'olymp_point'

    # Olymp title
    title: Mapped[OlympTitle] = mapped_column(sa.Enum, nullable=False)

    # Тип диплома участников
    grade: Mapped[Grades] = mapped_column(sa.Enum, nullable=False)

    # Баллы участников
    points: Mapped[float] = mapped_column(sa.Float, nullable=False)

    # Классы участников
    user_class: Mapped[Optional[int]] = mapped_column(sa.SmallInteger, nullable=True)

    # Имена участников
    names: Mapped[Optional[str]] = mapped_column(sa.String(100), nullable=True)

    # Регион участников
    region: Mapped[Optional[str]] = mapped_column(sa.String(100), nullable=True)

    # Школы участников
    school: Mapped[Optional[str]] = mapped_column(sa.String(100), nullable=True)
