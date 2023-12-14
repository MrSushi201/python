# 2878. Get the Size of a DataFrame
# DataFrame players:
# +-------------+--------+
# | Column Name | Type   |
# +-------------+--------+
# | player_id   | int    |
# | name        | object |
# | age         | int    |
# | position    | object |
# | ...         | ...    |
# +-------------+--------+

# Write a solution to calculate and display the number of rows and columns of player.
# Return the result as an array: [number of rows, number of columns].

# Define function / solution
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    df_size = list(players.shape)
    return df_size