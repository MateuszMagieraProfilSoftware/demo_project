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
        Game().how_many_players()




print(Game().start())