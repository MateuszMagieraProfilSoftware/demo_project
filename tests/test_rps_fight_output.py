import pytest
from game.Figures import Rock, Paper, Scissors, Result


@pytest.mark.parametrize("test_input,expected",
                         [
                            (Rock().fight(Scissors()),Result.WIN),
                            (Rock().fight(Paper()),Result.LOSS),
                            (Rock().fight(Rock()),Result.TIE)
                         ])
def test_rock(test_input,expected):
    assert test_input == expected



@pytest.mark.parametrize("test_input,expected",
                         [
                            (Paper().fight(Rock()),Result.WIN),
                            (Paper().fight(Scissors()),Result.LOSS),
                            (Paper().fight(Paper()),Result.TIE)
                         ])
def test_paper(test_input,expected):
    assert test_input == expected


@pytest.mark.parametrize("test_input,expected",
                         [
                             (Scissors().fight(Paper()),Result.WIN),
                             (Scissors().fight(Rock()),Result.LOSS),
                             (Scissors().fight(Scissors()),Result.TIE)
                         ])
def test_scissors(test_input, expected):
    assert test_input == expected
