# 2879. Display the First Three Row
# DateFrame: emplyees
# Write a solution to display the first 3 rows of this DataFrame.

# Define solution and function
import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    selected_rows = employees.head(3)
    return selected_rows