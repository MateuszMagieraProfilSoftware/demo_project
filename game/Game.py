# Stwórz klasę Game
# Użytkownik klasy może dodać graczy (żywych lub komputerowych) do gry
# Nie ma limitu ilości graczy
#
# Powinna mieć metodę start(), która uruchomi pętlę z grą
from game.Players import HumanPlayer,ComputerPlayer


class Game:
    players = []
    def add_player(self):
        while True:
            player_type = input('What kind of a player would '
                                    'you like to add (Human or Computer player? :  ').lower()
            if player_type == 'human' or player_type == 'computer':
                if player_type == 'human':
                    self.players.append(HumanPlayer())
                    break
                elif player_type == 'computer':
                    self.players.append(ComputerPlayer())
                    break
            else:
                continue
print(Game().add_player())