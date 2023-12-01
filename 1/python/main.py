def extract_first_last_digit(input_str: str) -> int:
    first = last = None
    for char in input_str:
        if char.isdigit():
            if first is None:
                first = char
            last = char

    return int(f"{first}{last}")


def main():
    with open('puzzle_input.txt') as puzzle_input:
        rows = puzzle_input.readlines()
        result = sum((extract_first_last_digit(row) for row in rows))
        print(f"The result of the day one of aoc 2023 is {result}")


if __name__ == '__main__':
    main()
