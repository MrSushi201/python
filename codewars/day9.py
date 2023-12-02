# Count of positive / Sum of negatives
# Given an array of integers.
# Return an array, where the first elements is the count of positive numbers.
# And the second element is sum of negative numbers.
# 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.
# Example: For input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# You should get [10, -65]

# Define function
def count_positives_sum_negatives(arr: list):
    new_arr = []
    count_pos, sum_neg = 0, 0

    # Case where input array is empty
    if len(arr) == 0:
        print(new_arr)
        return new_arr
    
    # Case where input array is not empty 
    elif len(arr) > 0:
        new_arr = [count_pos, sum_neg]

        for i in arr:
            if i > 0:
                new_arr[0] = new_arr[0] + 1
            elif i < 0:
                new_arr[1] = new_arr[1] + i

        print(new_arr)
        return new_arr
    
def count_positives_sum_negatives_another(arr: list):
    if not arr: return []
    count_pos, sum_neg = 0, 0
    for i in arr:
        if i > 0:
            count_pos += 1
        elif i < 0:
            sum_neg += i
    return [count_pos, sum_neg]

# Ones and Zeros
# Given an array of ones and zeros, convert the equivalent binary value to an integer.
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
# However, the arrays can have varying lengths, not just limited to 4.

# Define function
def binary_array_to_number(arr: list):
    # Case where arr is not an array
    if not arr: return []
    bit_str = ""

    # If arr is an array with some lengths
    for i in arr:
        bit_str = bit_str + str(i)
    
    value = int(bit_str, 2)
    print(bit_str, value)

    return value

def binary_array_to_number(arr: list):
    if not arr: return []
    else:
        value = int("".join(map(str, arr)), 2)
        print(arr, ":", value)
        return value

binary_array_to_number([0, 0, 0, 1])
binary_array_to_number([0, 0, 1, 0])