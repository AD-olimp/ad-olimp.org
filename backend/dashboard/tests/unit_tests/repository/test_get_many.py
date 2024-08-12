from contextlib import nullcontext as does_not_raise
import pytest
from src.models.dto.dashboard import DataFilter, BoundaryData
from src.service import BoundaryService, OlympDataService
from src.service.base import AbstractModel
from tests.conftest import get_session_test, event_loop


def get_expectations() -> list[list[AbstractModel]]:
    expectation = [
        [
            BoundaryData(winner_boundary_points=145.0, pre_winner_boundary_points=135.0,
                         years=2024, title='Высшая проба', user_class=11),
        ],
        [
        ]
    ]
    return expectation


def get_test_data() -> list[DataFilter]:
    test_data = [
        DataFilter(year=[2024, 2023], user_class=[11, 10], title=["Высшая проба"], step=["Заключительный"]),
        DataFilter(year=[2023], user_class=[9], title=["Сибириада"], step=["Заключительный"]),
    ]
    return test_data


@pytest.mark.usefixtures("event_loop")
class TestGetMany:
    @pytest.mark.parametrize(
        "test_id, data_filter, expectation",
        [
            (0, get_test_data()[0], does_not_raise()),
            (1, get_test_data()[1], does_not_raise())
        ]
    )
    @pytest.mark.asyncio
    async def test_get_many_boundary(self, test_id, data_filter, expectation):
        with expectation:
            result_data = await BoundaryService().get_many(data_filter=data_filter, session_getter=get_session_test)
            assert result_data == get_expectations()[test_id]

    # @pytest.mark.parametrize(
    #     "test_id, data_filter, expectation",
    #     *get_test_data()
    # )
    # @pytest.mark.asyncio
    # async def test_get_many_olymp(self, test_id, data_filter, expectation):
    #     ...
    #     # with expectation:
    #     #     result_data = await OlympDataService().get_many(data_filter=data_filter, session_getter=get_session_test)
    #     #     assert result_data == get_expectations()[test_id]

    # @pytest.mark.parametrize(
    #     "test_id, data_filter, expectation",
    #     *get_test_data()
    # )
    # @pytest.mark.asyncio
    # async def test_get_many_passing(self, data_filter, expectation):
    #     ...
