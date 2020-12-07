"""
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
"""

from functools import partial
import re


def validate_length(length_str):
    regex = re.compile(r"^(\d{0,1}\d\d)(in|cm)$")
    match = regex.match(length_str)
    if match:
        num, unit = match.groups()
        if unit == "cm":
            return 150 <= int(num) <= 193
        elif unit == "in":
            return 59 <= int(num) <= 76
        return False


def validate_hex_color(color_str):
    regex = re.compile("^#[0-9a-f]{6}$")
    return regex.match(color_str) is not None


def validate_num_within_range(start, end, num_str):
    try:
        num = int(num_str)
        return start <= num <= end
    except ValueError:
        return False


def validate_eye_color(color_str):
    return color_str in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def validate_passport_id(string):
    regex = re.compile("^[0-9]{9}$")
    return regex.match(string) is not None

REQUIRED_FIELDS = {
    "byr": partial(validate_num_within_range, 1920, 2002),
    "iyr": partial(validate_num_within_range, 2010, 2020),
    "eyr": partial(validate_num_within_range, 2020, 2030),
    "hgt": validate_length,
    "hcl": validate_hex_color,
    "ecl": validate_eye_color,
    "pid": validate_passport_id,
}


def get_fields_from_line(line_fields):
    current_fields = {}
    for field in line_fields:
        current_fields.update(dict([field.split(":")]))
    return current_fields


def get_passport_fields(passport_str):
    field_values = {}
    for pair in passport_str.split():
        field_values.update(dict([pair.split(":")]))
    return field_values


def validate_passport(passport_str):
    fields = get_passport_fields(passport_str)

    if not set(REQUIRED_FIELDS).issubset(fields):
        return False

    for field, value in fields.items():
        validator = REQUIRED_FIELDS.get(field, lambda s: True)
        if not validator(value):
            return False
    return True

def count_valid_passports_from_file():
    count = 0
    with open("day_4_input.txt") as file:
        current_passport = ""
        for line in file:
            if len(line.split()) == 0:
                #TODO add optional flag to perform shallow or deep check
                count += validate_passport(current_passport)
                current_passport = ""
                continue
            current_passport += line
        #end of file is ignored if there aren't new lines,
        # so last line and passport needs to be validated after EoF
        current_passport += line
        count += validate_passport(current_passport)
    return count


if __name__ == "__main__":
    print(count_valid_passports_from_file())
