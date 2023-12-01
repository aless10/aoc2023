DIGITS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def extract_first_last_digit(input_str: str) -> int:
    first = last = None
    number = ""
    for char in input_str:
        if char.isdigit():
            if first is None:
                first = char
            last = char
        else:
            number += char
            for key, value in DIGITS.items():
                if key in number:
                    if first is None:
                        first = value
                    last = value
                    number = ""

    return int(f"{first}{last}")


def extract_first_last_digit_pointers(input_str: str) -> int:
    first = last = None
    number_front = number_back = ""
    i = 0
    j = len(input_str)
    while i <= len(input_str) or j >= 0:
        if first is None:
            char_front = input_str[i]
            if char_front.isdigit():
                first = char_front
            else:
                number_front += char_front
                for key, value in DIGITS.items():
                    if key in number_front:
                        first = value
        if last is None:
            char_back = input_str[j - 1]
            if char_back.isdigit():
                last = char_back
            else:
                number_back = char_back + number_back
                for key, value in DIGITS.items():
                    if key in number_back:
                        last = value
        i += 1
        j += -1

    return int(f"{first}{last}")


def main():
    with open('puzzle_input.txt') as puzzle_input:
        rows = puzzle_input.readlines()
        for row in rows:
            extract_first_last_digit_pointers(row.replace("\n", ""))
        result = sum((extract_first_last_digit_pointers(row) for row in rows))
        print(f"The result of the day one of aoc 2023 is {result}")


if __name__ == '__main__':
    main()
