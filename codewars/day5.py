# MakeUpperCase
# Write a function which converts the input string to uppercase.

# Define function
def make_upper_case(s: str):
    res = s.upper()
    print(res)
    return res

# String Repeat
# Write a function that accepts an integer n, and a string s as parameters.
# Return a string of s repeated exactly n times. 
# Examples: Input --> Output
#           6, "I" --> "IIIIII"
#           5, "Hello" --> "HelloHelloHelloHelloHello"¨

# Define function
def repeat_str(n: int, s: str):
    res = s * n
    print(res)
    return res