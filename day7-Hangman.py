import random
import os
from Day7Hangmanpics import hang_man_pics
from Day7HangmanWordlist import word_list


chosen_word = random.choice(word_list)
chosen_word_list = []
spaces_list = []
wrong_counter = 0
guesses = []
user_guess = []

guess = False
complete = False
wrong_guess = False
loose = False
game_over = False
invalid_input = False

for letter in chosen_word:
    chosen_word_list.append(letter)
    spaces_list.append("_")

def print_function():
    global user_guess
    global game_over
    global wrong_counter
    print(hang_man_pics[wrong_counter])
    if invalid_input == True:
        print("Your input is invalid or you have inputted a letter twice!")
        print(f'You have already tried: {", ".join(guesses)}')
    if guess == True:
        print(f'You have already tried: {", ".join(guesses)}')
        print("Your Guess is in the word.")
    if complete == True:
        print("Congraduations, You Won, Game Over.")
        print("".join(spaces_list))
        game_over = True
    if wrong_guess == True:
        print(f"You have guessed wrong, you have {6 - wrong_counter} guesses left.")
        print(f'You have already tried: {", ".join(guesses)}')
    if complete == False:
        print(" ".join(spaces_list))
        user_guess = input("Guess a letter in the word.\n").lower()
    if loose == True:
        print(hang_man_pics[wrong_counter + 1])
        print("Out of Guesses, You Loose")
        print(" ".join(spaces_list))
        print(f'The word was \"{"".join(chosen_word_list)}\"')
        game_over = True


while game_over == False:
    os.system('cls')
    print_function()
    guess = False
    wrong_guess = False
    invalid_input = False
    if len(user_guess) > 1:
        invalid_input = True
    elif user_guess in guesses:
        invalid_input = True
    else:
        guesses.append(user_guess)
        for letter in range(len(chosen_word_list)):
            if user_guess == chosen_word_list[letter]:
                spaces_list[letter] = user_guess
                guess = True
        if user_guess not in spaces_list:
            wrong_counter += 1
            wrong_guess = True
            print(wrong_counter)
        if wrong_counter >= 5:
            loose = True
    if "_" not in spaces_list:
        complete = True
