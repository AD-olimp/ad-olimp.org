from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseTable
from src.models.common import OlympTitle


class PassingPointORM(BaseTable):
    """Проходные баллы на олимпиаду"""

    __tablename__ = 'passing_point'

    # Проходные баллы на олимпиаду (ось У)
    passing_points: Mapped[float] = mapped_column(sa.Float, nullable=False)

    # Даты проведения (ось Х)
    years: Mapped[int] = mapped_column(sa.Integer, nullable=False)

    # Название олимпиады
    title: Mapped[OlympTitle] = mapped_column(sa.Enum(OlympTitle), nullable=False)

    # Классы участников
    user_class: Mapped[Optional[int]] = mapped_column(sa.SmallInteger, nullable=True)
