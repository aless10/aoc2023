LIMITS = {
    "blue": 14,
    "green": 13,
    "red": 12
}


class Extraction:
    def __init__(self, extraction: dict[str: int]):
        self.extraction = extraction
        self.is_valid = self._is_valid()

    @classmethod
    def from_raw_string(cls, raw_string) -> 'Extraction':
        args = raw_string.split(",")
        """3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"""
        result = {}
        for arg in args:
            number, color = arg.strip().split(" ")
            result[color] = int(number)
        return cls(result)

    def _is_valid(self):
        for key, value in self.extraction.items():
            if value > LIMITS.get(key):
                return False
        return True


class Game:
    def __init__(self, id_: str, extractions: list[Extraction]):
        self.id = id_
        self.extractions = extractions

    @classmethod
    def from_raw_line(cls, raw_line):
        name, extractions = raw_line.split(":")
        id_ = name.split(" ")[1]
        extractions = extractions.split(";")
        extractions = [Extraction.from_raw_string(extraction) for extraction in extractions]
        return cls(id_, extractions)

    def is_game_possible(self):
        return all(extraction.is_valid for extraction in self.extractions)


def main():
    with open('puzzle_input.txt') as puzzle_input:
        rows = puzzle_input.readlines()
        valid_games = []
        for row in rows:
            game = Game.from_raw_line(row.replace("\n", ""))
            if game.is_game_possible():
                valid_games.append(int(game.id))
        result = sum(valid_games)
        print(f"The result of the day 2 of aoc 2023 is {result}")


if __name__ == '__main__':
    main()
