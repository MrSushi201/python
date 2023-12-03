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