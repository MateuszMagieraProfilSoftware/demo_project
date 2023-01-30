# Stwórz klasę Game
# Użytkownik klasy może dodać graczy (żywych lub komputerowych) do gry
# Nie ma limitu ilości graczy
#
# Powinna mieć metodę start(), która uruchomi pętlę z grą
import random

from game.Figures import Figure, FigureName, Result
from game.Players import HumanPlayer,ComputerPlayer


class Game:
    players = []
    result = None
    def add_player(self):
        human_player = self.players.append(HumanPlayer(username=input("Please provide your name: ")))
        comp_player = self.players.append(ComputerPlayer(username='Computer'))


    def start(self):
        figures = {}
        self.add_player()
        for player in self.players:
            figures[player.username] = player.get_figure()
        list_of_values = list(figures.values())
        if list_of_values[0].fight(list_of_values[1]) == Result.WIN:
            result = Result.WIN
            print(result)
        elif list_of_values[0].fight(list_of_values[1]) == Result.LOSS:
            result = Result.LOSS
            print(result)
        elif list_of_values[0].fight(list_of_values[1]) == Result.TIE:
            result = Result.TIE
            print(result)
        return figures

print(Game().start())







