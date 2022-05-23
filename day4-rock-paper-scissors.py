rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

# List to link the choice with the ACSII Art rps = Rock, Paper, Scissors.
rps_list = [rock, paper, scissors]
print_result = ""

# Winning Results Calculation Lists
#     R    P    S
R = ["D", "L", "W"]
P = ["W", "D", "L"]
S = ["L", "W", "D"]

# Nested List of the above table for the player_choice
nested_list = [R, P, S]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#Invalid Input Handling from player_choice
if player_choice > 2 or player_choice < 0:
  print("Invalid Choice.")
else:
  # Computer random choice
  computer_choice = random.randint(0, 2)
  
  # Going through the nested_list then into the "Winning Results Calculation Lists"
  result = nested_list[player_choice][computer_choice]
  
  # If Statements to display the result of the game
  if result == "D":
    print_result = "Draw"
  elif result == "L":
    print_result = "You Loose"
  elif result == "W":
    print_result = "You Win"
  
  # Printing of the Result of the Game
  print(f"{rps_list[player_choice]}\n Computer Chose:\n {rps_list[computer_choice]}\n{print_result}")