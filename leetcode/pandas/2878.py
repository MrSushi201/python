# 2878. Get the Size of a DataFrame
# DataFrame: players
# Write a solution to calculate and display the number of rows and columns of player.
# Return the result as an array: [number of rows, number of columns].

# Define solution and function
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    df_size = list(players.shape)
    return df_size