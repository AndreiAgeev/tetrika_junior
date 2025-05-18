import pytest

from functions import TestTask3
from constants import Task3Constants


@pytest.mark.parametrize(
    'intervals, answer', Task3Constants.SUCCESSFULL_TESTS
)
def test_successfull_answers(intervals, answer): 
    test_answer = TestTask3.sum_intervals(intervals)
    assert(
        test_answer == answer
    ), f'Ошибка теста. Получен результат {test_answer}, должен быть {answer}'


@pytest.mark.parametrize(
    'intervals', Task3Constants.UNSUCCESSFULL_TESTS
)
def test_unsuccessfull_answers(intervals):
    with pytest.raises(ValueError):
        TestTask3.sum_intervals(intervals)

