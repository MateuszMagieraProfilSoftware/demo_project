import pytest

from game.Figures import Figure
from game.Players import ComputerPlayer


def test_computer_choice():
    assert isinstance(ComputerPlayer().get_figure(),Figure)
