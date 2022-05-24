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
# Winning Results Calculation Lists (Player = Rows, Computer = Columns)
#    R    P    S
#R=["D", "L", "W"]
#P=["W", "D", "L"]
#S=["L", "W", "D"]
results_list = [
  ["Draw", "You Loose", "You Win"],
  ["You Win", "Draw", "You Loose"],
  ["You Loose", "You Win", "Draw"],
]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#Invalid Input Handling from player_choice
if player_choice > 2 or player_choice < 0:
  print("Invalid Choice.")
else:

  # Computer random choice
  computer_choice = random.randint(0, 2)

  #Navigating through the table to find the result.
  result = results_list[player_choice][computer_choice]
  
  # If Statements to display the result of the game
  if result == "Draw":
    print_result = "Draw"
  elif result == "You Loose":
    print_result = "You Loose"
  elif result == "You Win":
    print_result = "You Win"
  
  # Printing of the Result of the Game
  print(f"{rps_list[player_choice]}\n Computer Chose:\n {rps_list[computer_choice]}\n{print_result}")
