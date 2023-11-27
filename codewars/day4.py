# Basic Mathematical Operations
# Your task is to create a function that does four basic mathematical operations.
# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.
# Example: function(operator, value1, value2) --> output

# Define function
def basic_op(operator: str, value1: int | float, value2: int | float):
    if operator == "+":
        res = value1 + value2
        return res
    elif operator == "-":
        res = value1 - value2
        return res
    elif operator in ["*", "x"]:
        res = value1 * value2
        return res
    elif operator == "/":
        res = value1 / value2
        return res
    else:
        pass

# Define function
def basic_op_eval(operator: str, value1: int | float, value2: int | float):
    return eval(f"{value1}{operator}{value2}")