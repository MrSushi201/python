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