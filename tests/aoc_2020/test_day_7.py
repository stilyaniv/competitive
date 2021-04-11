import pytest
from src.aoc_2020 import day_7

DESCRIPTION = "light red bags contain 1 bright white bag, 2 muted yellow bags."
DESCRIPTION_NO_CONTENTS = "faded blue bags contain no other bags."
EXAMPLE_INPUT = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""


@pytest.fixture
def example_file_path(tmp_path):
    path = tmp_path / "day_7_test_input.txt"
    path.write_text(EXAMPLE_INPUT)
    return path


def test_parse_rule():
    expected = ["light red", "bright white", "muted yellow"]
    # expected = [("light red", "bright white"), ("light red", "muted yellow")]
    result = list(day_7.parse_rule(DESCRIPTION))
    assert result == expected


def test_parse_rule_no_contents():
    expected = ["faded blue", "no other"]
    result = list(day_7.parse_rule(DESCRIPTION_NO_CONTENTS))
    assert result == expected


def test_parse_rule_weights_no_contents():
    expected = [("", "faded blue"), ("", "no other")]
    result = list(day_7.parse_rule(DESCRIPTION_NO_CONTENTS, True))
    assert result == expected


def test_parse_rule_weights():
    expected = [("", "light red"), ("1", "bright white"), ("2", "muted yellow")]
    # expected = [('light red', 'bright white', '1'), ("light red", "muted yellow", "2")]
    # expected = {'light red': 'bright white', '1'), ("light red", "muted yellow", "2")]
    result = list(day_7.parse_rule(DESCRIPTION, include_weights=True))
    assert result == expected


def test_get_bag_contents_rules(example_file_path):
    expected = {
        "shiny gold": [("dark olive", 1), ("vibrant plum", 2)],
        "dark olive": [("faded blue", 3), ("dotted black", 4)],
        "vibrant plum": [("faded blue", 5), ("dotted black", 6)],
        "faded blue": [],
        "dotted black": [],
        "light red": [("bright white", 1), ("muted yellow", 2)],
        "dark orange": [("bright white", 3), ("muted yellow", 4)],
        "bright white": [("shiny gold", 1)],
        "muted yellow": [("shiny gold", 2), ("faded blue", 9)],
    }

    result = day_7.get_bag_contents_rules(example_file_path)
    assert result == expected


def test_count_ouetermost_bag_options(example_file_path):
    result = day_7.count_ouetermost_bag_options(example_file_path, "shiny gold")
    assert result == 4


def test_count_ouetermost_bag_options_challenge():
    result = day_7.count_ouetermost_bag_options(day_7.INPUT_FILE_PATH, "shiny gold")
    assert result == 101 


def test_count_inner_bags(example_file_path):
    result = day_7.count_inner_bags(example_file_path, "shiny gold")
    assert result == 32


def test_count_inner_bags_challenge():
    result = day_7.count_inner_bags(day_7.INPUT_FILE_PATH, "shiny gold")
    assert result == 108636
