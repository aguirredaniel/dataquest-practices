import pandas as pd


# - For the variables measured on a interval scale, add their names as a string to a list named interval. Sort the
#   list alphabetically.
# - For the variables measured on a ratio scale, add their names as a string to a list named ratio. Sort the list
#   alphabetically.
# - We've also added the Weight_deviation variable to the dataset, so make sure you include that one too in one of the
#   lists.
def main():
    wnba = pd.read_csv('wnba.csv')

    interval = sorted(['Birthdate', 'Weight_deviation'])
    ratio = sorted(['Height', 'Weight', 'BMI', 'Age', 'Experience', 'Games Played', 'MIN', 'FGM', 'FGA', 'FG%', '15:00',
                    '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TO', 'PTS', 'DD2',
                    'TD3'])


if __name__ == '__main__':
    main()
