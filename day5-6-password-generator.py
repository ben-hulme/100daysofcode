# Password Generator
# CHANGE: How long would the user like their password to be totally
# How many Symbols the user would like in the password
# How many Numbers the user would like in the password

import random
password = []
nr_letters = 0

#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_length = int(input("How long would you like your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

if (nr_length - nr_symbols) > nr_numbers:

  nr_letters = nr_length - (nr_symbols + nr_numbers)

  for letter_choice in range(1, nr_letters + 1):
    password += random.choice(letters)

  for symbol_choice in range(1, nr_symbols + 1):
    password.insert(random.randint(0, nr_letters - 1), symbols[random.randint(0, len(symbols) - 1)])

  for number_choice in range(1, nr_numbers + 1):
    password.insert(random.randint(0, (nr_letters + nr_symbols) - 1), numbers[random.randint(0, len(numbers) - 1)])

  password = "".join(password)
  print(password)
else:
  print("The number of Symbols and Numbers must be less than the total length of the Password.")
