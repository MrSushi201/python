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