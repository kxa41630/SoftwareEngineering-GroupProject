""" Guess the number game created by keerthi / Susmitha 
----------------------------------------
"""
import random
numOfattempts_list = []
def showThe_score():
    if len(numOfattempts_list) <= 0:
        print("There is no high score currently its will be your if you play!")
    else:
        print("The present high score is {} attempts".format(min(numOfattempts_list)))
def startThe_game():
    random_number = int(random.randint(1, 10))
    print("Hello gamer! Welcome to the game of guessing!")
    player_name = input("Enter your name? ")
    wantTo_play = input("Hi, {}, would you like to play the guessing the number game? (Enter Yes/No) ".format(player_name))
    
    attempts = 0
    showThe_score()
    while wantTo_play.lower() == "yes":
        try:
            guess = input("guess a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random_number:
                print("Nice! You won the game!")
                attempts += 1
                numOfattempts_list.append(attempts)
                print("It took you {}number of attempts".format(attempts))
                play_again = input("Would you like to play this game play again? (Enter Yes/No) ")
                attempts = 0
                showThe_score()
                random_number = int(random.randint(1, 10))
                if play_again.lower() == "no":
                    print("That's cool, have a good one!")
                    break
            elif int(guess) > random_number:
                print("It's lower")
                attempts += 1
            elif int(guess) < random_number:
                print("It's higher")
                attempts += 1
        except ValueError as err:
            print("Oh no!, that is not a valid value. please Try again...")
            print("({})".format(err))
    else:
        print("That's nice, have a good day!")
if __name__ == '__main__':
    startThe_game()