#program for calculator 
#This create empty list for calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y
 
def divide(x, y):
    if y == 0:
        return "Can't divide by zero"
    return x / y
#Main program
while True :
    print("Options:")
    print("Enter '+' for addition")
    print("Enter '-' for subtraction")
    print("Enter '*' for multiplication")
    print("Enter '/' for division")
    print("Enter 'quit' to end the program")

    user_input = input(" : ")
    
    if user_input == "quit":
        break

    operations = {
        '+' : add,
        '-' : subtract,
        '*' :multiply,
        '/' : divide
    }

    if user_input in operations:
        num1 = float(input("Enter First nimber:"))
        num2 = float(input("Enter second number: "))
        result = operations[user_input](num1, num2)
        print("Result:", result)
    else:
        print("Invalid Input.")
