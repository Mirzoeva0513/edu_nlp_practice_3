import task_2


tests: list[tuple[str, str]] = [
    ("с227на 69", "Тип 1А"),
    ("в555рх 39", "Тип 1А"),
    ("ао365 78", "Тип 1Б"),
    ("ан7331 47", "Тип 2"),
    ("3733мм 55", "Тип 3"),
]


def test_task_2():
    for plate, expected in tests:
        actual = task_2.get_plate_type(plate)
        assert expected == actual, plate
