from random import randrange


class WelcomeUser:

    def __int__(self):
        pass

    def welcome_user(self):
        user_name = input("Welcome, please enter your name:").capitalize()
        welcome_message = "Hello, " + user_name + " thank you for playing my game!!!"
        print(welcome_message)


class Paper:

    def strong_against(self):
        return 'Rock'

    def weak_against(self):
        return 'Scissors'


class Rock:
    def strong_against(self):
        return 'Scissors'

    def weak_against(self):
        return 'Paper'

class Scissors:
    def strong_against(self):
        return 'Paper'

    def weak_against(self):
        return 'Rock'


class ComputerBasicChoice:

    def __int__(self):
        pass

    def basic_figures(self):
        basic_figures = ['Paper','Rock','Scissors']
        return basic_figures[randrange(3)]


class UserChoice():

    def user_selected_figure(self):
        user_figure = input("Please select your figure: ").capitalize()
        return user_figure


class Fight(ComputerBasicChoice,UserChoice,Rock,Paper,Scissors):

    def decider(self):
        computer_figure = ComputerBasicChoice.basic_figures(ComputerBasicChoice)
        print(computer_figure)
        user_figure = UserChoice.user_selected_figure(UserChoice)
        if computer_figure == 'Rock':
            if user_figure == Rock.weak_against(Rock):
                print('User wins')
            elif computer_figure == user_figure:
                print("it's a tie")
            else:
                print('Computer wins')
        elif computer_figure == 'Paper':
            if user_figure == Paper.weak_against(Paper):
                print('User wins')
            elif computer_figure == user_figure:
                print("it's a tie")
            else:
                print('Computer wins')
        elif computer_figure == 'Scissors':
            if user_figure == Scissors.weak_against(Scissors):
                print('User wins')
            elif computer_figure == user_figure:
                print("it's a tie")
            else:
                print('Computer wins')

Fight.decider(self=None)