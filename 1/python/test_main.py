import pytest
from .main import extract_first_last_digit, extract_first_last_digit_pointers


@pytest.mark.parametrize("input_str, expected", [
    ("1abc2", 12),
    ("pqr3stu8vwx", 38),
    ("a1b2c3d4e5f", 15),
    ("treb7uchet", 77)
])
def test_extract_first_last_digit_part_one(input_str, expected):
    assert extract_first_last_digit(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("1abc2", 12),
    ("pqr3stu8vwx", 38),
    ("a1b2c3d4e5f", 15),
    ("treb7uchet", 77)
])
def test_extract_first_last_digit_part_one(input_str, expected):
    assert extract_first_last_digit_pointers(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("two1nine", 29),
    ("eightwothree", 83),
    ("abcone2threexyz", 13),
    ("xtwone3four", 24),
    ("4nineeightseven2", 42),
    ("zoneight234", 14),
    ("7pqrstsixteen", 76),
])
def test_extract_first_last_digit(input_str, expected):
    assert extract_first_last_digit_pointers(input_str) == expected
