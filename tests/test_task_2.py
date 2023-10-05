import task_2


tests: list[tuple[str, str]] = [
    ("с227на 69", "1А"),
    ("в555рх 39", "1А"),
    ("ао365 78", "1Б"),
    ("ан7331 47", "2"),
    ("3733мм 55", "3"),
]


def test_task_2():
    for plate, expected in tests:
        actual = task_2.get_plate_type(plate)
        assert expected == actual, plate
