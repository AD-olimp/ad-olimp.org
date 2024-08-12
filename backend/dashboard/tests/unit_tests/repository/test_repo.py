import pytest
from contextlib import nullcontext as does_not_raise

from src.models.dto.schemas_get.dashboard import BoundaryData
from src.service import BoundaryService
from tests.conftest import get_session_test, setup_db, event_loop


def get_test_data():
    test_data = [
        (BoundaryData(winner_boundary_points=145, pre_winner_boundary_points=135, years=2024,
                      title="Высшая проба", user_class=11), does_not_raise()),
        (BoundaryData(winner_boundary_points=160, pre_winner_boundary_points=155, years=2023,
                      title="Сибириада", user_class=10), does_not_raise())
    ]
    return test_data


@pytest.mark.usefixtures("event_loop", "setup_db")
class TestRepository:

    @pytest.mark.parametrize(
        "data, expectation",
        get_test_data()
    )
    @pytest.mark.asyncio
    async def test_insert(
            self,
            data,
            expectation
    ):
        with expectation:
            await BoundaryService().insert(data=data, session_getter=get_session_test)
            assert True

    @pytest.mark.parametrize(
        "ident, expected_data, expectation",
        [
            (31, *get_test_data()[1]),
            (32, *get_test_data()[0]),
        ]
    )
    @pytest.mark.asyncio
    async def test_get(self, ident, expected_data, expectation):
        with expectation:
            result_data = await BoundaryService().get(data_id=ident, session_getter=get_session_test)
            assert result_data == expected_data

    @pytest.mark.parametrize(
        "ident, new_data, expectation",
        [
            (31, *get_test_data()[1]),
            (32, *get_test_data()[0])
        ]
    )
    @pytest.mark.asyncio
    async def test_update(self, ident, new_data, expectation):
        with expectation:
            await BoundaryService().update(data_id=ident, new_data=new_data, session_getter=get_session_test)
            assert True

