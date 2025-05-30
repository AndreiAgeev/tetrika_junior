import inspect
from functools import wraps


def strict(func):
    error_wrong_type = (
        'Тип аргумента "{key}" не соответствует заявленному. '
        'Получен {value_type}, должен быть {expected_type}'
    )
    error_not_annotated = 'В функции аннотированы не все переменные.'

    @wraps(func)
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        if not annotations or len(annotations) != (len(args) + len(kwargs) + 1):
            raise TypeError(error_not_annotated)

        func_args = inspect.signature(func).bind(
            *args, **kwargs
        ).arguments.items()  # на случай использования именованных аргументов при вызове функции
        for key, value in func_args:
            expected_type = annotations.get(key)
            if type(value) is not expected_type:
                raise TypeError(
                    error_wrong_type.format(
                        key=key,
                        value_type=type(value).__name__,
                        expected_type=expected_type.__name__,
                    )
                )
        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    print(sum_two(1, 2))  # >>> 3
    # print(sum_two(1, 2.4))  # >>> TypeError
    print(sum_two(b=3, a=1))
    print(sum_two(4, b=2))
    print(sum_two(True, False))
    print(sum_two(b='str', a=3.14159265))
