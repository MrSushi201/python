# Sum of Positive
# You get an array of numbers, return the sum of all of the positive ones.
# If there is nothing to sum, the sum is default to 0.

# Define function/solution
def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum = sum + i
        elif i < 0:
            pass
    print(sum)
    return sum

def positive_sum(arr):
    pos_sum = sum(i for i in arr if i > 0)
    return pos_sum