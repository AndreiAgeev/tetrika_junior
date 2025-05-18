from functions import TestTask1

class Task1Constants:
    """
    Класс констант для тестов task1.

    Переменные:
        - SUCCESSFULL_TESTS: кортеж с данными, для успешных сценариев;
        - UNSUCCESSFULL_TESTS: кортеж с данными, для неуспешных сценариев.
    """
    SUCCESSFULL_TESTS = (
        (TestTask1.sum_two, (1, 2), 3),
        (TestTask1.concatenate_strings, ('foo', 'bar'), 'foobar'),
        (TestTask1.division, (4, 2), 2),
        (TestTask1.invert_bool, (True,), False),
    )
    UNSUCCESSFULL_TESTS = (
        (TestTask1.sum_two, (1, 2.5)),
        (TestTask1.concatenate_strings, ('foo', 123)),
        (TestTask1.division, (4, 'foo')),
        (TestTask1.invert_bool, (123,)),
        (TestTask1.not_annotated, (1, 2)),
    )


class Task3Constants:
    """
    Класс констант для тестов task3.

    Переменные:
        - SUCCESSFULL_TESTS: кортеж с данными, которые выдадут результат. Варианты:
            1) У одного из ползователей пустой список интервалов;
            2) У обоих пользователей пустые интервалы;
            3) Интервалы ученика и учителя не совпадают полностью;
            4) Полное совпадение всех трёх интервалов;
            5) У одного пользователя интервалы выходят за интервалы урока;
            6) У одного пользователя пропуски в интервалах;
            7) У одного пользователя есть перекрывающиеся интерваалы.
        - UNSUCCESSFULL_TESTS: кортеж с данными, которые вызовут ошибку ValueError. Варианты:
            1) Длина одного из интервалов не кратна двум;
            2) Интервал урока пустой.
    """
    SUCCESSFULL_TESTS = (
        ({'lesson': [3600, 7200], 'pupil': [3700, 7100], 'tutor': []}, 0),
        ({'lesson': [3600, 7200], 'pupil': [], 'tutor': []}, 0),
        ({'lesson': [3600, 7200], 'pupil': [3700, 5400], 'tutor': [5400, 7100]}, 0),
        ({'lesson': [3600, 7200], 'pupil': [3600, 7200], 'tutor': [3600, 7200]}, 3600),
        ({'lesson': [3600, 7200], 'pupil': [3000, 8000], 'tutor': [3600, 7200]}, 3600),
        (
            {
                'lesson': [3600, 7200],
                'pupil': [3700, 4000, 4100, 4400, 6900, 7200],
                'tutor': [3600, 7200]
            },
            900
        ),
        (
            {
                'lesson': [3600, 7200],
                'pupil': [3700, 5700, 4100, 4400, 6500, 7000, 6900, 7200],
                'tutor': [3600, 7200]
            },
            2700
        )
    )
    UNSUCCESSFULL_TESTS = (
        {'lesson': [3600, 7200], 'pupil': [3700], 'tutor': []},
        {'lesson': [], 'pupil': [3700, 7100], 'tutor': [3700, 7100]},
    )
