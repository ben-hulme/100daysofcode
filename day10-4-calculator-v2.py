import os

continue_calculation = True

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

print(f"Please enter what you would like to calculate.\nYou can enter your input as '25+86' or 25 + 86:")

def calculator():

    calculation = input(":")

    cal_num = ""
    calculation_list = []

    for data in calculation:
        if data in operation_dict:
            if cal_num != "":
                calculation_list.append(float(cal_num))
                cal_num = ""
            calculation_list.append(data)
        if data not in operation_dict:
            cal_num += data

    calculation_list.append(float(cal_num))

    result = operation_dict[calculation_list[1]](calculation_list[0], calculation_list[2])

    print(f"{calculation_list[0]} {calculation_list[1]} {calculation_list[2]} = {result}")
    calculator()

calculator()