from typing import List

from game.rock_paper_scissors_v2 import FigureName, Result


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
