from unittest.mock import patch

import pytest
import requests
from _pytest.monkeypatch import monkeypatch

from game.Figures import Figure
from game.Players import ComputerPlayer,HumanPlayer


def test_computer_choice():
    assert isinstance(ComputerPlayer().get_figure(),Figure)

@pytest.mark.parametrize('test_input',['Rock','Paper','Scissors'])
def test_user_choice(monkeypatch,test_input):
    monkeypatch.setattr('builtins.input', lambda _: test_input)
    result = HumanPlayer().get_figure()
    assert isinstance(result,Figure)