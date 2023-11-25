# Sentence Smash
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. 
# You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. 
# Be careful, there shouldn't be a space at the beginning or the end of the sentence!
# Example: ["Hello", "world", "this", "is", "great"] => "Hello world this is great"

# Define function
def smash(words):
    if len(words) == 0:
        text = ""
        print("Argument is empty...")
        return text
    elif len(words) >= 1:
        text = " "
        result = text.join(words)
        print(result)
        return result

# Test
lst = ["Hello", "world", "this", "is", "great"]
smash(lst)