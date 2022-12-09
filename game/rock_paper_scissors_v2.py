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


class Rock:
    figure_name = FigureName.ROCK.value
    strong_against = [FigureName.SCISSORS.value]
    weak_against = [FigureName.PAPER.value]

    def fight(self, other_figure):
        if other_figure in Rock.strong_against:
            return Result.WIN
        elif other_figure == Rock.figure_name:
            return Result.TIE
        elif other_figure in Rock.weak_against:
            return Result.LOSS
        else:
            raise RuntimeError('Unrecognized figure')


class Paper:
    figure_name = FigureName.PAPER.value
    strong_against = [FigureName.ROCK.value]
    weak_against = [FigureName.SCISSORS.value]

    def fight(self,other_figure):
        if other_figure in Paper.strong_against:
            return Result.WIN
        elif other_figure == Paper.figure_name:
            return Result.TIE
        elif other_figure in Paper.weak_against:
            return Result.LOSS
        else:
            raise RuntimeError('Unrecognized figure')


class Scissors:
    figure_name = FigureName.SCISSORS.value
    strong_against = [FigureName.PAPER.value]
    weak_against = [FigureName.ROCK.value]

    def fight(self,other_figure):
        if other_figure in Scissors.strong_against:
            return Result.WIN
        elif other_figure == Scissors.figure_name:
            return Result.TIE
        elif other_figure in Scissors.weak_against:
            return Result.LOSS
        else:
            raise RuntimeError('Unrecognized figure')


rock = Rock()
paper = Paper()
scissors = Scissors()

print(paper.fight('ROCK'))
print(rock.fight("ROCK"))
print(scissors.fight('ROCK'))