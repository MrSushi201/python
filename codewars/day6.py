# Even or Odd
# Create a function that takes an integer as an argument.
# Return "Even" for even numbers or "Odd" for odd numbers.

# Define function
def even_or_odd(number: int):
    if number % 2 == 0:
        return "Even"
    elif number % 2 != 0:
        return "Odd"
    else:
        pass

# Count by X
# Create a function with two arguments that will return an array of the first n multiples of x.
# Assume both given number and the number of times to count will be positive numbers greater than 0.
# Return the results as an array or list. 
# Examples: count_by(1, 10) # should return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#           count_by(2, 5) # should return [2, 4, 6, 8, 10]¨

# Define function
def count_by(x: int, n: int):
    if (x or n) <= 0:
        raise ValueError("Both x and n must be greater than 0")
    elif (x and n) > 0:
        lst = [x * i for i in range(1, n + 1)]
        print(lst)
        return lst
    
count_by(1, 10)
count_by(2, 5)