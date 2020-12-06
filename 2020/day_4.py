from functools import partial
import re


def validate_length(lengthStr):
    r = re.compile(r"^(\d{0,1}\d\d)(in|cm)$")
    match = r.match(lengthStr)
    if match:
        num, unit = match.groups()
        if unit == "cm":
            return 150 <= int(num) <= 193
        elif unit == "in":
            return 59 <= int(num) <= 76
        return False


def validate_hex_color(colorStr):
    r = re.compile("^#[0-9a-f]{6}$")
    return r.match(colorStr) is not None


def validate_num_within_range(start, end, numStr):
    try:
        num = int(numStr)
        return start <= num <= end
    except ValueError:
        return False


def validate_eye_color(colorStr):
    return colorStr in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def validate_passport_id(string):
    r = re.compile("^[0-9]{9}$")
    return r.match(string) is not None


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
REQUIRED_FIELDS = {
    "byr": partial(validate_num_within_range, 1920, 2002),
    "iyr": partial(validate_num_within_range, 2010, 2020),
    "eyr": partial(validate_num_within_range, 2020, 2030),
    "hgt": validate_length,
    "hcl": validate_hex_color,
    "ecl": validate_eye_color,
    "pid": validate_passport_id,
}


def get_fields_from_line(lineFields):
    currentFields = {}
    for field in lineFields:
        currentFields.update(dict([field.split(":")]))
    return currentFields


def get_passport_fields(passportStr):
    fieldsValues = {}
    for pair in passportStr.split():
        fieldsValues.update(dict([pair.split(":")]))
    return fieldsValues


def validate_passport(passportStr):
    fields = get_passport_fields(passportStr)

    if not set(REQUIRED_FIELDS).issubset(fields):
        return False

    for field, value in fields.items():
        validator = REQUIRED_FIELDS.get(field, lambda s: True)
        if not validator(value):
            return False
    return True


if __name__ == "__main__":
    count = 0
    with open("day_4_input.txt") as file:
        currentPassport = ""
        for line in file:
            if len(line.split()) == 0:
                count += validate_passport(currentPassport)
                currentPassport = ""
                continue
            currentPassport += line
        #end of file is ignored if there aren't new lines, 
        # so last line and passport needs to be validated after EoF
        currentPassport += line
        count += validate_passport(currentPassport)

    print(count)
