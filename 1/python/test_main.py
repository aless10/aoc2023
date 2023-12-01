import pytest
from main import extract_first_last_digit


@pytest.mark.parametrize("input_str, expected", [
    ("1abc2", 12),
    ("pqr3stu8vwx", 38),
    ("a1b2c3d4e5f", 15),
    ("treb7uchet", 77)
])
def test_extract_first_last_digit(input_str, expected):
    assert extract_first_last_digit(input_str) == expected
