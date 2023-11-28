"""
Lesson 2: variables
Variables contain data. So, you can call them later. 
This makes data reusable, recallable, re-assignable et cetera. 
It is crucial to understand variables. 
Simplest definition of a variable is a "named container" of data you would like to refer to in your program. 
It is hard to imagine programming without variables as we use them to identify and refer to data of different sizes, types, and shapes. 
Let us try to understand the step-by-step:
    1. First, a variable with a name is created. 
    And then, an integer object with a value is assigned to the variable as its value. 
    Vice versa, an integer object with a value is created. 
    And later, assigned to a variable with a name.
    "value" -> "variable" # Read as an object is assigned with a variable name.
    "variable" -> "value" # Read as a variable name is assigned to an object.

    2. A new value is assigned to the variable, and now, it has a new value. 
    Also, the old value is lost.
"""

# Example on how to store object(s) to variable(s)
var = "value" # var -> "value"
print(var)
i, j, k = [1, 0, 0], [0, 1, 0], [0, 0, 1]
print(i, j, k)

# Exercise 2-a: Mix number and text inside the print()-function
glass_of_water = 3
print("I drank", glass_of_water, "glasses of water everyday.")

# Exercise 2-b: Assign a new value to an existing variable
glass_of_water = 3
print(id(glass_of_water))
glass_of_water = glass_of_water + 1
print(id(glass_of_water))