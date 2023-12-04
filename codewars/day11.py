# Friend or Foe?
# Make a program that filers a list of strings and returns a list with only your friends name in it.
# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!
# Otherwise, you can be sure he is not. 
# Example:
# Input = ["Ryan", "Kieran", "Jason", "Yous"] --> Output = ["Ryan", "Yous"]
# Note: Keep the original order of the names in the output.

# Define function / solution
def friend(x: list):
    friend_list = [i for i in x if len(i) == 4]
    print(friend_list)
    return friend_list 