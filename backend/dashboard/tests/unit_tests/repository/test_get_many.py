from contextlib import nullcontext as does_not_raise
import pytest
from src.models.dto.schemas_get.dashboard import DataFilter
from src.service import BoundaryService
from tests.conftest import get_session_test, event_loop


@pytest.mark.usefixtures("event_loop")
class TestGetMany:
    @pytest.mark.parametrize(
        "year, user_class, title, step, expectation",
        [
            ([2024, 2023], [11, 10], ["Высшая проба"], ["Заключительный"], does_not_raise()),
            ([2023], [9], ["Сибириада"], ["Заключительный"], does_not_raise())
        ]
    )
    @pytest.mark.asyncio
    async def test_get_many_boundary(self, year, user_class, title, step, expectation):
        with expectation:
            data_filter = DataFilter(year=year, user_class=user_class, title=title, step=step)
            result_data = await BoundaryService().get_many(data_filter=data_filter, session_getter=get_session_test)
            assert result_data == []

    @pytest.mark.parametrize(
        "year, user_class, title, step, expectation",
        [
            ([2024, 2023], [11, 10], ["Высшая проба"], ["Заключительный"], does_not_raise()),
            ([2023], [9], ["Сибириада"], ["Заключительный"], does_not_raise())
        ]
    )
    async def test_get_many_olymp(self, year, user_class, title, step, expectation):
        ...

    @pytest.mark.parametrize(
        "year, user_class, title, step, expectation",
        [
            ([2024, 2023], [11, 10], ["Высшая проба"], ["Заключительный"], does_not_raise()),
            ([2023], [9], ["Сибириада"], ["Заключительный"], does_not_raise())
        ]
    )
    async def test_get_many_passing(self, year, user_class, title, step, expectation):
        ...
