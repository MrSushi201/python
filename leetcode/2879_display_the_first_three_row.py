# 2879. Display the First Three Row
# DataFrame: employees
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | employee_id | int    |
# | name        | object |
# | department  | object |
# | salary      | int    |
# +-------------+--------+
# Write a solution to display the first 3 rows of this DataFrame.

# Define function / solution
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    selected_rows = employees.head(3)
    return selected_rows