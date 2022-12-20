from enum import Enum
from typing import List

class Result(Enum):
    WIN = 1
    LOSS = -1
    TIE = 0


class FigureName(Enum):
    ROCK = "ROCK"
    PAPER = "PAPER"
    SCISSORS = "SCISSORS"
    LIZARD = "LIZARD"
    SPOCK = "SPOCK"


class Figure:
    figure_name : FigureName
    strong_against: List[FigureName]

    def fight(self,other_figure: 'Figure'):
        if self.figure_name in other_figure.strong_against:
            return Result.LOSS
        elif other_figure.figure_name in self.strong_against:
            return Result.WIN
        elif other_figure.figure_name == self.figure_name:
            return Result.TIE
        else:
            raise RuntimeError("Unrecognized figure")

class Rock(Figure):
    figure_name = FigureName.ROCK
    strong_against = [FigureName.SCISSORS]

class Paper(Figure):
    figure_name = FigureName.PAPER
    strong_against = [FigureName.ROCK]

class Scissors(Figure):
    figure_name = FigureName.SCISSORS
    strong_against = [FigureName.PAPER]
class NameToClass:
    name_to_class_mapping = {
        FigureName.ROCK.value: Rock(),
        FigureName.PAPER.value: Paper(),
        FigureName.SCISSORS.value: Scissors()}


