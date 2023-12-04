from .main import Game, Extraction


def test_extraction_valid():
    _extraction = """3 blue, 4 red"""
    extraction = Extraction.from_raw_string(_extraction)
    assert extraction.extraction == {
        "blue": 3,
        "red": 4
    }
    assert extraction.is_valid


def test_extraction_not_valid():
    _extraction = """8 green, 6 blue, 20 red"""
    extraction = Extraction.from_raw_string(_extraction)
    assert extraction.extraction == {
        "blue": 6,
        "red": 20,
        "green": 8
    }
    assert not extraction.is_valid


def test_game():
    _game = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"""
    game = Game.from_raw_line(_game)
    assert game.id == "1"
    assert [e.extraction for e in game.extractions] == [
            {
                "blue": 3,
                "red": 4
            },
            {
                "red": 1,
                "green": 2,
                "blue": 6
            },
            {
                "green": 2,
            },
    ]


def test_is_game_possible():
    _game = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"""
    game = Game.from_raw_line(_game)
    assert game.is_game_possible()


def test_is_game_possible_fail():
    _game = """Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"""
    game = Game.from_raw_line(_game)
    assert not game.is_game_possible()
