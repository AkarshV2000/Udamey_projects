#   ** Calculator **
import os
def clear_console():
    os.system('cls')


def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations= {
"+" : add,
"-" : subtract,
"*" : multiply,
"/" : divide
}

def Calculator():
    num1= float(input("Enter a number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:

        operation_symbol = input("Enter a operation:  ")
        num2 = float(input("Enter the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if (input(f"type 'y' to continue calculation with {answer}, or type 'n' to exit: ")) == "y":
            num1= answer
        else:
            should_continue = False
            clear_console()
Calculator()




    
