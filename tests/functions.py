from task1.solution import strict
from task3.solution import appearance


class TestTask1:

    @staticmethod
    @strict
    def sum_two(a: int, b: int) -> int:
        return a + b

    @staticmethod
    @strict
    def concatenate_strings(a: str, b: str) -> str:
        return a + b

    @staticmethod
    @strict
    def division(a: int, b: int) -> float:
        return a/b

    @staticmethod
    @strict
    def invert_bool(a: bool) -> bool:
        return not a

    @staticmethod
    @strict
    def not_annotated(a: int, b):
        return a + b


class TestTask3:

    @staticmethod
    def sum_intervals(intervals: dict[str, list[int]]) -> int:
        return appearance(intervals)
