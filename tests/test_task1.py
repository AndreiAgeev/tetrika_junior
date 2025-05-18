import pytest

from functions import TestTask1
from constants import Task1Constants


@pytest.mark.parametrize(
    'func, args, expected_result', Task1Constants.SUCCESSFULL_TESTS
)
def test_successfull(func, args, expected_result):
    """Проверяем успешные сценарии test1."""
    assert func(*args) == expected_result


@pytest.mark.parametrize(
    'func, args', Task1Constants.UNSUCCESSFULL_TESTS
)
def test_unsuccessfull(func, args):
    """Проверяем неуспешные сценарии test1."""
    with pytest.raises(TypeError):
        func(*args)
