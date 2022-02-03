import numpy as np
from scipy.stats import chisquare, chi2_contingency
import pandas as pd


def chi_squared(observed, expected):
    return (observed - expected) ** 2 / expected


# - Use the scipy.stats.chi2_contingency function to calculate the p-value for the sex and race columns of income.
# - Assign the result to pvalue_gender_race.
def main():
    income = pd.read_csv('income.csv')

    table = pd.crosstab(income["sex"], [income["race"]])
    chi2, pvalue_gender_race, dof, expected = chi2_contingency(table)

    print(chi2, pvalue_gender_race, dof, expected, sep='\n')


if __name__ == '__main__':
    main()
