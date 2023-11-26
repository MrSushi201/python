# Simple Multiplication
# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

# Define function
def simple_multiplication(number):
    if (number % 2) == 0:
        print("The argument is an EVEN number...")
        res = number * 8
        print(f"{res} is the product of {number} times 8.")
        return res
    elif (number % 2) != 0:
        print("The argument is an ODD number...")
        res = number * 9
        print(f"{res} is the product of {number} times 9")
        return res
    
simple_multiplication(8)