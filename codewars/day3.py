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

# Invert values
# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.

# Define function
def invert(lst):
    new_lst = [-x for x in lst]
    print(f"Inverse of given list: {new_lst}")
    return new_lst