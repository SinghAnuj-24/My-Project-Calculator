#Simple Calculator for 
print("Welcome to Simple Calculator")

try:
    Number1 = float(input("Enter First number: "))
except ValueError:
    print("Invalid input! Please enter a number.")
try:
    Number2 = float(input("Enter Second number: "))
except ValueError:
    print("Invalid input! Please enter a number.")

operator = input("Select the operator:")
if operator == "+":
    print("Sum of {} and {} is {}".format(Number1  , Number2 , Number1 + Number2))
elif operator == "-":   
    print("Subtraction of {} and {} is {}".format(Number1  , Number2 , Number1 - Number2))
elif operator == "%":   
    print("Modulus of {} and {} is {}".format(Number1  , Number2 , Number1 % Number2))
elif operator == "/":
    if Number2 == 0:
        print("Error! Cannot divide by zero.")
    else:
        print("Division of {} and {} is {}".format(Number1, Number2, Number1 / Number2))
elif operator == "%":
    print("Modulus of {} and {} is {}".format(Number1, Number2, Number1 % Number2))
elif operator == "*":
    print("Multiply of {} and {} is {}".format(Number1, Number2, Number1 * Number2))
else: 
    print("Invalid choice! Please select a valid operator")