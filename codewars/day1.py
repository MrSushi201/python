# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# Example: for [1, 2, 2], it should return 9 because 1^2 + 2^2 + 2^2 = 9

# Define function
def square_sum(nums):
    sq_sum = sum((_ * _) for _ in nums)
    return sq_sum, print(f"Sum of square(nums): {sq_sum}")

square_sum([1, 2, 2])

# We need a function that can transform a number (integer) into a string.
# Example: (input --> output)
# 123 --> "123"
# 999 --> "999"
# -100 --> "-100"
def num_to_str(num):
    if num != None:
        text = str(num)
        return text, print(f"Integer to convert: {text}. Type after conversion: {type(text)}")
    else:
        pass

num_to_str(-100)