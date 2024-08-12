from sqlalchemy import Integer, MetaData
from sqlalchemy.orm import as_declarative
from sqlalchemy.orm import Mapped, declared_attr, mapped_column


metadata = MetaData()


@as_declarative(metadata=metadata)
class BaseTable:
    """Abstract model with declarative base functionality."""
    __allow_unmapped__ = False

    id: Mapped[int] = mapped_column(
        Integer, autoincrement=True, primary_key=True
    )
