# Return Negative
# In this simple assignment, you are given a number and have to make it negative.
# But maybe the number is already negative?
# Examples: 
#           make_negative(1) --> -1
#           make_negative(-5) --> -5
#           make_negative(0) --> 0
# NOTE 1: The number can be negative already, in which case no change is required.
# NOTE 2: Zero(0) is not checked for any specific sign. Negative zeros make no mathematical sense.

# Define function
def make_negative(number: int or float):
    if number >= 0:
        res = -1 * number
        print(res)
        return res
    else:
        res = number
        print(res)
        return res
    
# Century From Year
# The first century spans from the year 1 up to and including the year 100. 
# The second century spans from 101 up to and including the year 200, et cetera.
# Task:
#       Given a year, return the century it is in.
# Examples:
            # 1705 --> 18
            # 1900 --> 19
            # 1601 --> 17
            # 2000 --> 20

# Define function
def century(year: int):
    if year <= 0:
        pass
    elif year > 0:
        res = ((year - 1) // 100) + 1
        print(res)
        return res
