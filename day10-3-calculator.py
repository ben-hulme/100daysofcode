import os

# Calculator Operations
#Add
def add(n1, n2):
    return n1 + n2
#Subtract
def subtract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1 / n2

#Operation User Selection to Function Dictionary
operation_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    keep_going = True

    first_number = float(input("What's the first number?: "))
    for op in operation_dict:
        print(op)

    while keep_going:
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        result = operation_dict[operation](first_number, second_number)
        print(f"{first_number} {operation} {second_number} = {result}")
        continue_calc = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if continue_calc == "y":
            first_number = result
        else:
            keep_going = False
            os.system('cls')
            calculator()

calculator()