import pytest
from src.aoc_2020 import day_4

INVALID_PASSPORT_1 = """
    eyr:1972 cid:100
    hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
"""

INVALID_PASSPORT_2 = """
    iyr:2019
    hcl:#602927 eyr:1967 hgt:170cm
    ecl:grn pid:012533040 byr:1946
"""

INVALID_PASSPORT_3 = """
    hcl:dab227 iyr:2012
    ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
"""

INVALID_PASSPORT_4 = """
    hgt:59cm ecl:zzz
    eyr:2038 hcl:74454a iyr:2023
    pid:3556412378 byr:2007
"""

VALID_PASSPORT_1 = """
    pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
    hcl:#623a2f
"""

VALID_PASSPORT_2 = """
    eyr:2029 ecl:blu cid:129 byr:1989
    iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
"""

VALID_PASSPORT_3 = """
    hcl:#888785
    hgt:164cm byr:2001 iyr:2015 cid:88
    pid:545766238 ecl:hzl
    eyr:2022
"""

VALID_PASSPORT_4 = """
iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

EXAMPLE_INPUT_PART_1 = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

EXAMPLE_INPUT_PART_2 = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""


@pytest.fixture
def example_file_path_part_1(tmp_path):
    path = tmp_path / "day_4_test_input.txt"
    path.write_text(EXAMPLE_INPUT_PART_1)
    return path


@pytest.fixture
def example_file_path_part_2(tmp_path):
    path = tmp_path / "day_4_test_input.txt"
    path.write_text(EXAMPLE_INPUT_PART_2)
    return path


def test_count_valid_passports_from_file_non_strict(example_file_path_part_1):
    result = day_4.count_valid_passports_from_file(example_file_path_part_1)
    assert result == 2


def test_count_valid_passports_from_file_strict(example_file_path_part_2):
    result = day_4.count_valid_passports_from_file(
        example_file_path_part_2, check_field_values=True
    )
    assert result == 4


def test_get_passport_fields():
    expected = {
        "eyr": "1972",
        "cid": "100",
        "hcl": "#18171d",
        "ecl": "amb",
        "hgt": "170",
        "pid": "186cm",
        "iyr": "2018",
        "byr": "1926",
    }
    assert expected == day_4.get_passport_fields(INVALID_PASSPORT_1)


def test_validate_passport_invalid():
    assert not day_4.validate_passport(INVALID_PASSPORT_1, check_field_values=True)
    assert not day_4.validate_passport(INVALID_PASSPORT_2, check_field_values=True)
    assert not day_4.validate_passport(INVALID_PASSPORT_3, check_field_values=True)
    assert not day_4.validate_passport(INVALID_PASSPORT_4, check_field_values=True)


def test_validate_passport_valid():
    assert day_4.validate_passport(VALID_PASSPORT_1, check_field_values=True)
    assert day_4.validate_passport(VALID_PASSPORT_2, check_field_values=True)
    assert day_4.validate_passport(VALID_PASSPORT_3, check_field_values=True)
    assert day_4.validate_passport(VALID_PASSPORT_4, check_field_values=True)


def test_validate_num_within_range_valid():
    assert day_4.validate_num_within_range(1990, 2010, "1990")
    assert day_4.validate_num_within_range(1990, 2010, "2000")
    assert day_4.validate_num_within_range(1990, 2010, "2010")


def test_validate_num_within_range_invalid():
    assert not day_4.validate_num_within_range(1990, 2010, "2021")
    assert not day_4.validate_num_within_range(1990, 2010, "1989")
    assert not day_4.validate_num_within_range(1990, 2010, "0990")


def test_validate_length_valid_inches():
    assert day_4.validate_length("60in")


def test_validate_length_valid_cm():
    assert day_4.validate_length("190cm")


def test_validate_length_invalid_too_many_inches():
    assert not day_4.validate_length("190in")


def test_validate_length_invalid_no_unit():
    assert not day_4.validate_length("190")


def test_validate_eye_color_valid():
    assert day_4.validate_eye_color("brn")


def test_validate_eye_color_invalid():
    assert not day_4.validate_eye_color("wat")


def test_validate_hex_color_valid():
    assert day_4.validate_hex_color("#123abc")


def test_validate_hex_color_invalid_wrong_chars():
    assert not day_4.validate_hex_color("#123abz")


def test_validate_hex_color_invalid_wrong_no_hash():
    assert not day_4.validate_hex_color("123abc")


def test_validate_passport_id_valid():
    assert day_4.validate_passport_id("000000001")


def test_validate_passport_id_invalid_too_long():
    assert not day_4.validate_passport_id("0123456789")


def test_validate_passport_id_invalid_too_short():
    assert not day_4.validate_passport_id("00012345")
