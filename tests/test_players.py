import pytest
from game.Players import HumanPlayer,ComputerPlayer,Player

@pytest.mark.parametrize("test_input,expected",
                         [
                             (issubclass(HumanPlayer,Player),
                              issubclass(ComputerPlayer,Player)
                              )
                         ])
def test_players(test_input,expected):
    assert test_input == expected