# 2880. Select Data
# DataFrame: students
# Write a solution to select the name and age of student with student_id = 101.

# Define function
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    data = students.loc[students["student_id"] == 101, ["name", "age"] ]
    return data