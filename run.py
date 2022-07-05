import random


def user_details():
    """
    The user enter his/her name
    As well as a breakdown of the rules of the game.
    """
    name = (input("\
Please enter your name or we will call you player. \n")).strip() or ' player'
    print(f"Hello,{name} are you ready to play a game of morra.")
    print("In this game you need to guess the computers number.")
    print("While the computer guesses your number.")
    print("You have to choose between 1, 2 and 3. ")
    print('The first person to reach 12 wins.')
    print()
    game_choice()


def game_choice():
    """
    Here we are going to ask the user to input a number
    between 1 and 3.
    The computer will randomize a number between 1 and 3.
    Then we will compare the two numbers to see if they
    are the same or different.
    """
    player_score = 0
    comp_score = 0
    while True:
        try:
            user_choice = int(input("Choose a number between 1 and 3: \n"))
            if user_choice not in range(1, 3):
                print("Please enter a number between 1 and 3")
                user_choice = int(input("Choose a number between 1 and 3: \n"))
            else: 
                computer_guess = random.randint(1, 3)
                print(f"The computer chose: {computer_guess}\n")
        except ValueError:
            print("Please enter a valid number")       
        

user_details()