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
    game_mode = None
    counter = {"player": 0,
               "computer": 0
               }

    def choose_game_version(self):
        game_version = input("Which mode would you like to play, basic or advanced? :  ")
        self.game_mode = game_version.lower()
        return self.game_mode

    def add_player(self):
        human_player = self.players.append(HumanPlayer(username=input("Please provide your name: ")))
        comp_player = self.players.append(ComputerPlayer(username='Computer'))


    def play_game(self):
        figures = {}
        self.add_player()
        self.choose_game_version()
        if self.game_mode == 'basic':
            for player in self.players:
                figures[player.username] = player.get_figure()
        elif self.game_mode == 'advanced':
            for player in self.players:
                figures[player.username] = player.get_advanced_figure()
        list_of_values = list(figures.values())
        if list_of_values[0].fight(list_of_values[1]) == Result.WIN:
            result = Result.WIN
            self.counter["player"] += 1
            print(result)
        elif list_of_values[0].fight(list_of_values[1]) == Result.LOSS:
            result = Result.LOSS
            self.counter["computer"] += 1
            print(result)
        elif list_of_values[0].fight(list_of_values[1]) == Result.TIE:
            result = Result.TIE
            print(result)
        return figures
    def start_game(self):
        while True:
            self.play_game()
            print(self.counter)
            play_again = input("Would you like to play again? (yes/no): ").lower()
            if play_again =='no':
                print(self.counter)
                break



print(Game().start_game())







