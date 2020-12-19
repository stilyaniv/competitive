import pytest
import day_8

EXAMPLE_INPUT = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

OP_TUPLES = [
    ("nop", +0),
    ("acc", +1),
    ("jmp", +4),
    ("acc", +3),
    ("jmp", -3),
    ("acc", -99),
    ("acc", +1),
    ("jmp", -4),
    ("acc", +6),
]


@pytest.fixture
def example_file_path(tmp_path):
    path = tmp_path / "day_8_test_input.txt"
    path.write_text(EXAMPLE_INPUT)
    return path


def test_load_operations_from_file(example_file_path):
    assert day_8.load_operations_from_file(example_file_path) == OP_TUPLES


def test_execute_code_file(example_file_path):
    assert day_8.execute_code_file(example_file_path) == 5


def test_execute_code():
    assert day_8.execute_code(OP_TUPLES) == 5


def test_execute_and_fix_code():
    assert day_8.execute_and_fix_code(OP_TUPLES) == 8
