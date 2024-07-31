"""Chat model file."""
from typing import Optional

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import BaseTable
from src.models.common import OlympTitle


class BoundaryPointORM(BaseTable):
    """Граничные баллы на победителя и призера на олимпиаде"""

    __tablename__ = 'boundary_point'

    # Граничные баллы на победителя (ось У)
    winner_boundary_points: Mapped[float] = mapped_column(sa.Float, nullable=False)

    # Граничные баллы на призера (ось У)
    pre_winner_boundary_points: Mapped[float] = mapped_column(sa.Float, nullable=False)

    # Даты проведения (ось Х)
    years: Mapped[int] = mapped_column(sa.Integer, nullable=False)

    # Название олимпиады
    title: Mapped[OlympTitle] = mapped_column(sa.Enum, nullable=False)

    # Класс участников
    user_class: Mapped[Optional[int]] = mapped_column(sa.SmallInteger, nullable=True)
