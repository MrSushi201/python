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