from sqlalchemy import and_, ColumnElement

from src.models.dto.dashboard import OlympDataFilter, PassingDataFilter
from src.models.orm import OlympORM, BoundaryPointORM, PassingPointORM


def convert_to_statement_olymp(data_filter: OlympDataFilter) -> ColumnElement[bool]:
    stmt = and_(
        OlympORM.title.in_(data_filter.title),
        OlympORM.user_class.in_(data_filter.user_class),

    )
    return stmt


def convert_to_statement_boundary(data_filter: OlympDataFilter) -> ColumnElement[bool]:
    stmt = and_(
        BoundaryPointORM.title.in_(data_filter.title),
        BoundaryPointORM.user_class.in_(data_filter.user_class),
        BoundaryPointORM.years.in_(data_filter.year)
    )
    return stmt


def convert_to_statement_passing(data_filter: PassingDataFilter) -> ColumnElement[bool]:
    stmt = and_(
        PassingPointORM.years.in_(data_filter.year),
        PassingPointORM.title.in_(data_filter.title),
        PassingPointORM.user_class.in_(data_filter.user_class)
    )
    return stmt
