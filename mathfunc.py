import numpy as np

def mainf():
    print("Welcome to the advanced math program")
    print("Please enter the operation you would like to perform")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponent")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mult()
    elif choice == 4:
        div()
    elif choice == 5:
        exp()
    elif choice == 6:
        sqrt()
    elif choice == 7:
        log()
    elif choice == 8:
        sin()
    elif choice == 9:
        cos()
    elif choice == 10:
        tan()
    elif choice == 11:
        pass
    else:
        print("Invalid choice")
        

def add():
    print("Addition")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The sum is: ", num1 + num2)
    

def sub():
    print("Subtraction")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The difference is: ", num1 - num2)
   

def mult():
    print("Multiplication")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The product is: ", num1 * num2)
    

def div():
    print("Division")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("The quotient is: ", num1 / num2)
    

def exp():
    print("Exponent")
    num1 = int(input("Enter base number: "))
    num2 = int(input("Enter exponent: "))
    print("The result is: ", num1 ** num2)
   

def sqrt():
    print("Square Root")
    num1 = int(input("Enter number: "))
    print("The square root is: ", np.sqrt(num1))
    

def log():
    print("Logarithm")
    num1 = int(input("Enter number: "))
    print("The logarithm is: ", np.log(num1))
    

def sin():
    print("Sine")
    num1 = int(input("Enter number: "))
    print("The sine is: ", np.sin(num1))
    

def cos():
    print("Cosine")
    num1 = int(input("Enter number: "))
    print("The cosine is: ", np.cos(num1))
    

def tan():
    print("Tangent")
    num1 = int(input("Enter number: "))
    print("The tangent is: ", np.tan(num1))
    