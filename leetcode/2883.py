# 2883. Drop Missing Data
# DataFrame: students
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | student_id  | int    |
# | name        | object |
# | age         | int    |
# +-------------+--------+
# There are some rows having missing values in the name column.
# Write a solution to remove the rows with missing values.
# The result format is in the following example.

# Define function / solution
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(axis = 0, subset = ["name"])