# You Cam't Code Under Pressure #1
# Code as fast as you can! You need to double the integer and return it. 

# Define function / solution
def double_integer(i):
    return (i + i)

# Mumbling
# This time, no story, no theory. The examples below show you how to write the function 'accum'.
# Examples:
#   accum("abcd") -> "A-Bb-Ccc-Dddd"
#   accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# The parameters of accum is a string which includes ONLY letters from a...z and A...Z.

# Define function / solution
def accum_1(s):
    if s.isalpha() == True:
        res = ""
        count = 0
        for i in s:
            res = res + (i + (i * count) + "-").capitalize()
            count = count + 1
        res = res[:-1]
        print(res)
        return res
    else:
        pass

accum_1("abcd")
accum_1("ZpglnRxqenU")

# Alternative
def accum_2(s):
    if s.isalpha() == True:
        res = "-".join((a * i).capitalize() for i, a in enumerate(s, 1))
        print(res)
        return res
    else:
        pass

accum_2("abcd")
accum_2("ZpglnRxqenU" )