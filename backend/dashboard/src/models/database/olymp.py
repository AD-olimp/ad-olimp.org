"""Chat model file."""
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from ...models.dashboard import OlympTitles


class Olymp(Base):
    """Chat model."""

    # Chat telegram id
    chat_id: Mapped[int] = mapped_column(sa.BigInteger, unique=True, nullable=False)

    # Olymp title
    title: Mapped[OlympTitles] = mapped_column(sa.Enum, nullable=False)


    step: Step  # Этап олимпиады
    grade: list[Grades]  # Диплом участников
    points: list[Point]  # Баллы участников
    user_class: Optional[list[int]]  # Классы участников
    names: Optional[list[str]]  # Имена участников
    region: Optional[list[str]]  # Регион участников
    school: Optional[list[str]]  # Школы участников
    passing_point: Optional[Point]  # Граничный балл

    #
    chat_type: Mapped[str] = mapped_column(sa.Text, unique=False, nullable=False)

    #
    title: Mapped[str] = mapped_column(sa.Text, unique=False, nullable=True)

    #
    chat_name: Mapped[str] = mapped_column(sa.Text, unique=False, nullable=True)

    #
    chat_user: Mapped[int] = mapped_column(sa.ForeignKey('user.id', ondelete='CASCADE'), unique=False, nullable=True)
