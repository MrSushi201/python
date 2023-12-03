# Reverse Words
# Complete the function that accepts a string parameter, and reverses each word in the string. 
# All spaces in th string should be retained.
# Examples: 
#   "This is an example!" ==> "sihT si na !elpmaxe"
#   "double  spaces"      ==> "elbuod  secaps"

# Define function
text = "I wonder how this text looks like backwards"
def reverse_words(text: str):
    text_split = text.split(" ")
    reverse_text = " ".join((x[::-1] for x in text_split))
    return reverse_text

reverse_words(text)

# Highest and Lowest
# You are given a string of space separated numbers, and have to return the highest and lowest number. 
# Examples:
#   high_and_low("1 2 3 4 5") # Return "5 1"
#   high_and_low("1 2 -3 4 5") # Return "5 -3"

# Define function
def high_and_low(numbers):
    if type(numbers) == str:
        string_split = numbers.split(" ")
        int_list = [int(number) for number in string_split]
        int_list.sort(reverse = True)
        return f"{int_list[0]} {int_list[-1]}"
    else:
        pass