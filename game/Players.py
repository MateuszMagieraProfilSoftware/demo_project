import random

from game.Figures import NameToClass


class Player:
    def __init__(self,username):
        self.username = username
    def get_figure(self):
        raise NotImplementedError

class HumanPlayer(Player):
    def get_figure(self):
        selected = None
        while not selected:
            selected = NameToClass.name_to_class_mapping.get(input('Select a figure: ').upper())
            if not selected:
                print('Incorrect input,please select again (rock,paper or scissors): ')
        return selected


class ComputerPlayer(Player):
    def get_figure(self):
        computer_figures = [value for value in NameToClass.name_to_class_mapping.values()]
        return random.choice(computer_figures)


# print(HumanPlayer().get_figure().fight(ComputerPlayer().get_figure()))