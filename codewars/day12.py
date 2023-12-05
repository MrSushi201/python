# Growth of a Population
# The population is p0 = 1000 at the beginning of a year.
# The population increases by 1000 * 0.02 per year. 
# The population also has a fixed increase of 50 new inhabitants per year.
# How many year does it take for the population to be greater than or equal to p = 1200?
# Examples:
#   nb_year(1500, 5, 100, 5000) -> 15

# Define function / solution
def nb_year(p0: int, percent: int | float, aug: int, p: int):
    current_p = p0
    n = 0

    while current_p < p:
        current_p = int(current_p + (percent / 100) * current_p + aug)
        n = n + 1

    return n