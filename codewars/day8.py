# String ends with?
# Complete the solution so that it returns True if the first argument(string) passed in ends with the 2nd argument (also a string).
# Examples:
#   solution('abc', 'bc') # True
#   solution('abc', 'd') # False

# Define function
def solution(text: str, ending: str):
    if (ending in text) and ending[-1] == text[-1]:
        print('True')
        return True
    else:
        return False
    
def solution(text:str, ending: str):
    if text.endswith(ending):
        return True
    else:
        return False
    
# You are a square
# Given an integral number, determine if it is a square number:
# In mathematics, a square number or perfect square is an integer that is the square of an integer;
# In other words, it is the product of some integer with itself.

# Define function
def is_square(n: int):
    square = n ** 0.5
    if square ** 2 == n:
        print("True")
        return True
    else:
        print("False")
        return False