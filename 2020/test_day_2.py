import day_2

def test_is_valid_pass_in_range_min():
    assert day_2.is_valid_pass_in_range("1-3 a: abcde")

def test_is_valid_pass_in_range_invalid():
    assert not day_2.is_valid_pass_in_range("1-3 b: cdefg")

def test_is_valid_pass_in_range_max():
    assert day_2.is_valid_pass_in_range("2-9 c: ccccccccc")

def test_count_valid_passwords_range():
    assert 439 == day_2.count_valid_passwords_range()

def test_is_valid_pass_xor_valid():
    assert day_2.is_valid_pass_xor("1-3 a: abcde")

def test_is_valid_pass_xor_neither():
    assert not day_2.is_valid_pass_xor("1-3 b: cdefg")

def test_is_valid_pass_xor_both():
    assert not day_2.is_valid_pass_xor("2-9 c: ccccccccc")

def test_count_valid_passwords_xor():
    assert 584 == day_2.count_valid_passwords_xor()