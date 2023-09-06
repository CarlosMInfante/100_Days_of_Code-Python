#Number Guessing Game Objectives:
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(player_guess, computer_number, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if player_guess > computer_number:
        print("Too high")
        return turns - 1
    elif player_guess < computer_number:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {computer_number}.")

def set_difficulty():
    """Sets the difficulty of the game."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


print(logo)
def game():
    computer_number = randint(1, 100)
    print("Welcome to the guessing game.")
    print("I'm thinking of a number between 1 and 100.")

    turns = set_difficulty()    

    player_guess = 0
    while player_guess != computer_number:     
        print(f"You have {turns} attempts remianing to guess the number.")   
        player_guess = int(input("Make a guess: "))
        turns = check_answer(player_guess, computer_number, turns)
        if turns == 0:
            print("Game Over!")
            return

game()
