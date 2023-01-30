import unittest.mock as mock
from game.Figures import Figure, FigureName, Result
from game.Game import Game
from game.Players import HumanPlayer, ComputerPlayer
import pytest

from unittest.mock import Mock, patch

def test_username(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'John')

    game = Game()
    game.add_player()

    assert game.players[0].username == 'John'


input_mock_username = mock.Mock()
input_mock_username.return_value = 'John'
input_mock_figure = mock.Mock()
input_mock_figure.return_value = 'rock'
input_mock = mock.Mock()
input_mock.side_effect = [input_mock_username.return_value,input_mock_figure.return_value]
def test_start():
    with mock.patch('builtins.input', input_mock) as mock_method:
        Game().start()
        assert Game().players[0] == 'John'
        assert Game.result in [Result.WIN,Result.LOSS, Result.TIE]
