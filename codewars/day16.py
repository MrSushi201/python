# Square Every Digit
# Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
# For example, if we run 9119 through the function, 811181 will come out. 
# Becaue, 9^2 is 81, and 1^2 is 1 (81-1-1-81).
# Again, 765 will/should return 493625 because 7^2 is 49, 6^2 36, and 5^2 is 25 (49-36-25).

# Define function / solution
def square_digits(num: int):
    num = str(num)
    res_lst = [str(int(i) ** 2) for i in num]
    res = int("".join(res_lst))
    return res