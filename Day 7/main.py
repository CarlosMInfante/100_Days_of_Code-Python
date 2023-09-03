# Hangman different steps
import random
import os
from hangman_art import logo, stages
from hangman_words import word_list

# Starting the game
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False
print(logo)

# Testing code
# print(chosen_word)

# Create blanks
display = []
for letter in range(word_length):
    display += "_"
print(display)

# Check guessed letter
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    os.system('cls')

    if guess in display:
        print(f"You already guessed {guess}.")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessd {guess}, that's not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])
