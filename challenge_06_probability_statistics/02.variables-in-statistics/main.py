import pandas
import pandas as pd


def main():
    wnba = pandas.read_csv('wnba.csv')
    variables = {'Name': 'qualitative', 'Team': 'qualitative', 'Pos': 'qualitative', 'Height': 'quantitative',
                 'BMI': 'quantitative', 'Birth_Place': 'qualitative', 'Birthdate': 'quantitative',
                 'Age': 'quantitative', 'College': 'qualitative', 'Experience': 'quantitative',
                 'Games Played': 'quantitative', 'MIN': 'quantitative', 'FGM': 'quantitative', 'FGA': 'quantitative',
                 '3PA': 'quantitative', 'FTM': 'quantitative', 'FTA': 'quantitative', 'FT%': 'quantitative',
                 'OREB': 'quantitative', 'DREB': 'quantitative', 'REB': 'quantitative', 'AST': 'quantitative',
                 'PTS': 'quantitative'}
