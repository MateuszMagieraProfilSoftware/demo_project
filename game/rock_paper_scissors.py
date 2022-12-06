from random import randrange
class WelcomeUser:

    def __int__(self):
        pass

    def welcome_user(self):
        user_name = input("Welcome, please enter your name:").capitalize()
        welcome_message = "Hello, " + user_name + " thank you for playing my game!!!"
        print(welcome_message)


class Paper:

    def paper_attributes(self):
        strong_against = 'Rock'
        weak_against = 'Scissors'
        return strong_against,weak_against


class Rock:

    def rock_attributes(self):
        strong_against = 'Scissors'
        weak_against = 'Paper'
        return strong_against,weak_against


class Scissors:
    def scissors_attributes(self):
        strong_against = 'Paper'
        weak_against = ' Rock'
        return strong_against,weak_against


class Lizard:
    def lizard_attributes(self):
        strong_against = 'Spock'
        weak_against = ' Scissors'
        return strong_against,weak_against


class Spock:
    def spock_attributes(self):
        strong_against = ['Scissors','Rock']
        weak_against = ['Lizard','Paper']
        return strong_against,weak_against

class ComputerBasicChoice:
    def __int__(self):
        pass
    def basic_figures(self):
        basic_figures = ['Paper','Rock','Scissors']
        return basic_figures[randrange(3)]


class UserChoice(Rock,Paper,Scissors):
    def __int__(self,rock_attributes):
        self.rock_attributes = rock_attributes

    def user_choice(self):
        user_choice = input("What mode would you prefer basic or advanced? :").capitalize()
        if user_choice == "Basic":
            print('Basic')
            save_user_choice = input("Please select your figure")
            return save_user_choice
        else:
            raise RuntimeError("No such mode, please re-run the game and select the correct modem")

class Fight(ComputerBasicChoice,UserChoice):
    def fight(self):
        user_choice = UserChoice.user_choice()
        computer_choice = ComputerBasicChoice.basic_figures()
        return user_choice,computer_choice



WelcomeUser.welcome_user(self=None)
UserChoice.user_choice(self=None)
print(ComputerBasicChoice.basic_figures(self=None))
