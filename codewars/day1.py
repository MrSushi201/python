# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# Example: for [1, 2, 2], it should return 9 because 1^2 + 2^2 + 2^2 = 9

# Define function
def square_sum(nums):
    sq_num = sum((_ * _) for _ in nums)
    return sq_num, print(f"Sum of square(nums): {sq_num}")

square_sum([1, 2, 2])