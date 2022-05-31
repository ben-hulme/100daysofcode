import random

computer_number = random.randint(0, 100)
guessed = False

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    guesses = 10
else:
    guesses = 5

def high_low(feedback):
    print(f"Too {feedback}.")
    if guesses > 1:
        print("Guess again")
    else:
        print(f"Game Over the answer was: {computer_number}")
    return guesses - 1

while guesses > 0 and not guessed:
    print(f"You have {guesses} attempts remaining to guess the number.")
    player_guess = int(input("Make a guess: "))
    if player_guess > computer_number:
        guesses = high_low("high")
    elif player_guess < computer_number:
        guesses = high_low("low")
    elif player_guess == computer_number:
        print(f"You got it! The answer was {computer_number}")
        guessed = True