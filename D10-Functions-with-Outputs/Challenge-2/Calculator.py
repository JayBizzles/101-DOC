#Calculator

def add(n1,n2):
    return n1 + n2

def multiply(n1,n2):
    return n1*n2

def subtract(n1,n2):
    return n1-n2
    
def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "x": multiply,
    "/": divide
}

def calculator():
    cont = True

    num1 = int(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What is the second number?: "))
    calculation_function = operations[operation_symbol]
    first_answer = calculation_function(num1,num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    while(cont):
        operation_symbol = input("Pick an operation from the line above: ")
        num3 = int(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        second_answer = calculation_function(first_answer,num3)
        print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
        usrinput = input("If you would like to continue with prev. # (y = yes),  (n = no)")
        if usrinput =="y":
            cont = True
        else:
            cont = False
            calculator() #takes us back to the top of the calculator where we can add new values



