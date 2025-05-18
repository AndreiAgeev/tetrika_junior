def merge_intervals(intervals: list[int]) -> list[list[int, int]]:
    """
    Функция объединения интервалов на тот случай, когда они пересекаются между собой.
    Если в функцию передан пустой список интервалов, то возрващает его без проверки.
    """
    result = list()
    if not intervals:
        return result
    user_intervals = [[intervals[i], intervals[i + 1]] for i in range(0, len(intervals), 2)]
    result.append(user_intervals[0])
    for new_interval in user_intervals[1:]:
        last_interval = result[-1]
        if new_interval[0] <= last_interval[1]:
            last_interval[1] = max(last_interval[1], new_interval[1])
        else:
            result.append(new_interval)
    return result


def user_intervals_during_lesson(
        user_intervals: list[list[int, int]], lesson_interval: list[int]
) -> list[tuple[int, int]]:
    """
    Функция опеределяет точные интервалы, когда пользователь был активен на платформе.
    Если в функцию передан пустой список интервалов юзера, то возрващает его без проверки.
    """
    result = list()
    if not user_intervals:
        return result
    lesson_start, lesson_end = lesson_interval
    for start, end in user_intervals:
        if start >= lesson_end or end <= lesson_start:
            continue
        result.append((max(start, lesson_start), min(end, lesson_end)))
    return result


def get_intersected_intervals(
    tutor_intervals: list[tuple[int, int]], pupil_intervals: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    """Функция определяет пересекающиеся интервалы ученика и учителя."""
    result = list()
    tutor_index = pupil_index = 0
    while tutor_index < len(tutor_intervals) and pupil_index < len(pupil_intervals):
        start = max(tutor_intervals[tutor_index][0], pupil_intervals[pupil_index][0])
        end = min(tutor_intervals[tutor_index][1], pupil_intervals[pupil_index][1])
        if start < end:
            result.append((start, end))
        if tutor_intervals[tutor_index][1] < pupil_intervals[pupil_index][1]:
            tutor_index += 1
        else:
            pupil_index += 1
    return result


def appearance(intervals: dict[str, list[int]]) -> int:
    for key, interval in intervals.items():
        if len(interval) % 2:
            raise ValueError(
                f'Длина списка интервалов {key} не кратна двум.'
            )
    if not intervals['lesson']:
        raise ValueError(
            f'Переданный список интервалов урока lesson пуст.'
        )
    tutor_intervals = user_intervals_during_lesson(
        merge_intervals(intervals['tutor']), intervals['lesson']
    )
    pupil_intervals = user_intervals_during_lesson(
        merge_intervals(intervals['pupil']), intervals['lesson']
    )
    result_intervals = get_intersected_intervals(tutor_intervals, pupil_intervals)
    return sum([end - start for start, end in result_intervals])


tests = [
    {
        "intervals": {
            "lesson": [1594663200, 1594666800],
            "pupil": [
                1594663340,
                1594663389,
                1594663390,
                1594663395,
                1594663396,
                1594666472,
            ],
            "tutor": [1594663290, 1594663430, 1594663443, 1594666473],
        },
        "answer": 3117,
    },
    {
        "intervals": {
            "lesson": [1594702800, 1594706400],
            "pupil": [
                1594702789,
                1594704500,
                1594702807,
                1594704542,
                1594704512,
                1594704513,
                1594704564,
                1594705150,
                1594704581,
                1594704582,
                1594704734,
                1594705009,
                1594705095,
                1594705096,
                1594705106,
                1594706480,
                1594705158,
                1594705773,
                1594705849,
                1594706480,
                1594706500,
                1594706875,
                1594706502,
                1594706503,
                1594706524,
                1594706524,
                1594706579,
                1594706641,
            ],
            "tutor": [
                1594700035,
                1594700364,
                1594702749,
                1594705148,
                1594705149,
                1594706463,
            ],
        },
        "answer": 3577,
    },
    {
        "intervals": {
            "lesson": [1594692000, 1594695600],
            "pupil": [1594692033, 1594696347],
            "tutor": [1594692017, 1594692066, 1594692068, 1594696341],
        },
        "answer": 3565,
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['intervals'])
        assert (
            test_answer == test['answer']
        ), f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
