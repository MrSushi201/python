# 2881. Create a New Column
# DataFrame: employees
# Write a solution to create new column name 'bonus' that contains the double values of the 'salary' column.
# Input:
# DataFrame employees
# +---------+--------+
# | name    | salary |
# +---------+--------+
# | Piper   | 4548   |
# | Grace   | 28150  |
# | Georgia | 1103   |
# | Willow  | 6593   |
# | Finn    | 74576  |
# | Thomas  | 24433  |
# +---------+--------+
# Output:
# +---------+--------+--------+
# | name    | salary | bonus  |
# +---------+--------+--------+
# | Piper   | 4548   | 9096   |
# | Grace   | 28150  | 56300  |
# | Georgia | 1103   | 2206   |
# | Willow  | 6593   | 13186  |
# | Finn    | 74576  | 149152 |
# | Thomas  | 24433  | 48866  |
# +---------+--------+--------+

# Define function
import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees