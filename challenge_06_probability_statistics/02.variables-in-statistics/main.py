import pandas as pd


# - In the code editor, we've already extracted for you the names of the variables that are measured on ratio and
#   interval scales. Every variable name is registered as a dictionary key.
# - If a variable is discrete, then assign the string 'discrete' to its corresponding dictionary key.
# - If a variable is continuous, then assign the string 'continuous' to its corresponding dictionary key.
def main():
    wnba = pd.read_csv('wnba.csv')

    ratio_interval_only = {'Height': 'continuous', 'Weight': 'continuous', 'BMI': 'continuous', 'Age': 'continuous',
                           'Games Played': 'discrete', 'MIN': 'continuous', 'FGM': 'discrete', 'FGA': 'discrete',
                           'FG%': 'continuous', '3PA': 'discrete', '3P%': 'continuous', 'FTM': 'discrete',
                           'FTA': 'discrete', 'FT%': 'continuous', 'OREB': 'discrete', 'DREB': 'discrete',
                           'REB': 'discrete', 'AST': 'discrete', 'STL': 'discrete', 'BLK': 'discrete', 'TO': 'discrete',
                           'PTS': 'discrete', 'DD2': 'discrete', 'TD3': 'discrete', 'Weight_deviation': 'continuous'}


if __name__ == '__main__':
    main()
