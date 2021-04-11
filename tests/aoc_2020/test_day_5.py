from src.aoc_2020 import day_5

def test_get_seat_info():
    assert (70, 7, 567) == day_5.get_seat_info("BFFFBBFRRR")
    assert (14, 7, 119) == day_5.get_seat_info("FFFBBBFRRR")
    assert (102, 4, 820) == day_5.get_seat_info("BBFFBBFRLL")

def test_get_missing_id_from_file():
    assert 615 == day_5.get_missing_id_from_file()


def test_get_max_id_from_file():
    assert 953 == day_5.get_max_id_from_file()