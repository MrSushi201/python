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