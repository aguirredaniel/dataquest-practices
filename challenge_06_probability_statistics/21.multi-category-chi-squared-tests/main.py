import numpy as np
from scipy.stats import chisquare
import pandas as pd


def chi_squared(observed, expected):
    return (observed - expected) ** 2 / expected


# - Use the pandas.crosstab function to print out a table comparing the sex column of income to the race column of
#   income.
def main():
    income = pd.read_csv('income.csv')

    table = pd.crosstab(income["sex"], [income["race"]])
    print(table)


if __name__ == '__main__':
    main()
