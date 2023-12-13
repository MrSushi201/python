# Abbreviate a Two World Name
# Write a function to convert a name into initials. 
# This kata strictly takes two words with one space in between them. 
# The output should be two capital letters with a dot separating them.
# It should look like this:
#   Sam Harris => S.H
#   patrick feeney => P.F

# Define function/solution
def abbrev_name(name):
    name_split = name.split(" ", 1)
    name_initials = (name_split[0][0] + "." + name_split[1][0]).upper()
    print(name_initials)
    return name_initials

def abbrev_name(name):
    first_name, last_name = name.split(" ", 1)
    initials = f"{first_name[0].upper()}.{last_name[0].upper()}"
    print(initials)
    return initials

def abbrev_name(name):
    res = ".".join(i[0] for i in name.split()).upper()
    print(res)
    return res