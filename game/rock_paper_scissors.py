class WelcomeUser:

    def __int__(self):
        pass

    @staticmethod
    def welcome_user():
        user_name = input("Welcome, please enter your name:").capitalize()
        welcome_message = "Hello, " + user_name + " thank you for playing my game!!!"
        print(welcome_message)


class Paper:

    @staticmethod
    def paper_attributes():
        strong_against = 'Rock'
        weak_against = 'Scissors'
        return strong_against,weak_against


class Rock:

    @staticmethod
    def rock_attributes():
        strong_against = 'Scissors'
        weak_against = 'Paper'
        return strong_against,weak_against


class Scissors:

    @staticmethod
    def scissors_attributes():
        strong_against = 'Paper'
        weak_against = ' Rock'
        return strong_against,weak_against




class UserChoice(Rock,Paper,Scissors):

    @staticmethod
    def user_choice():
        user_choice = input("What mode would you prefer basic or advanced? :").capitalize()
        if user_choice == "Basic":
            print("You are playing a basic mode, please select one of the three figures "
                  "rock, paper or scissors")
            user_figure = input("Please select your figure :").capitalize()
            # check attributes of BasicFiguresAttributes for rock to see what it is strong and weak against
            # Invoke a method outputting computer's choice here
            if user_figure == "Rock":
                print("You selected rock")
                print("A rock is strong against " + Rock.rock_attributes()[0])
                print("A rock is weak against " + Rock.rock_attributes()[1])
            elif user_figure == "Paper":
                print("You selected paper")
                print("The paper is strong against " + Paper.paper_attributes()[0])
                print("The paper is weak against " + Paper.paper_attributes()[1])
            elif user_figure == "Scissors":
                print("You selected scissors")
                print("Scissors are strong against " + Scissors.scissors_attributes()[0])
                print("Scissors are weak against " + Scissors.scissors_attributes()[1])
            else:
                raise RuntimeError("Incorrect figure")
        elif user_choice == "Advanced":
            #Lizard,spock tec logic here
            print("You are playing an advanced mode")
        else:
            raise RuntimeError("No such mode, please re-run the game and select the correct modem")


WelcomeUser.welcome_user()
UserChoice.user_choice()

