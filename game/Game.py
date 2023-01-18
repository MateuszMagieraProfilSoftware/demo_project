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
    def add_player(self):
        while True:
            player_type = input('What kind of a player would '
                                    'you like to add (Human or Computer player? :  ').lower()
            if player_type == 'human' or player_type == 'computer':
                if player_type == 'human':
                    self.players.append(HumanPlayer(username=input("Please provide the username: ")))
                    break
                elif player_type == 'computer':
                    self.players.append(ComputerPlayer(username=None))
                    break
            else:
                continue
    def how_many_players(self):
        while True:
            how_many_players = input('How many players would you like to add? : ')
            if int(how_many_players) < 2:
                print('There cannot be less than 2 players, please try again')
                continue
            for _ in range(int(how_many_players)):
                Game().add_player()
            break

    def start(self):
        figures_to_remove = []
        players_and_choices = {}
        Game().how_many_players()
        print(len(self.players))
        for player in self.players:
            players_and_choices[player.username] = player.get_figure()
        for figure1 in list(players_and_choices.values()):
            for figure2 in list(players_and_choices.values()):
                if figure1.fight(figure2) == Result.WIN:
                    figures_to_remove.append(figure2)
                elif figure1.fight(figure2) == Result.LOSS:
                    figures_to_remove.append(figure1)
                elif figure1.fight(figure2) == Result.TIE:
                    continue
        keys_to_remove = [key for key, value in players_and_choices.items() if value in figures_to_remove]
        for key in keys_to_remove:
            del players_and_choices[key]
        return players_and_choices











print(Game().start())