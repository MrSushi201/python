# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# Define function
def square_sum(nums):
    sq_num = sum((_ * _) for _ in nums)
    return sq_num, print(f"Sum of square(nums): {sq_num}")

square_sum([1, 2, 3])