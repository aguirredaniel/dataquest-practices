import numpy as np
from scipy.stats import chisquare


def chi_squared(observed, expected):
    return (observed - expected) ** 2 / expected


# - Use the scipy.stats.chisquare function to find the chi-squared value and p-value for the above observed and expected
#   counts.
# - Assign the p-value to pvalue_gender_income.
def main():
    males_over50k = .241 * .67 * 32561
    males_under50k = 0.759 * .67 * 32561
    females_over50k = 0.241 * .33 * 32561
    females_under50k = 0.759 * .33 * 32561

    observed_values = [6662, 15128, 1179, 9592]
    expected_values = [males_over50k, males_under50k, females_over50k, females_under50k]

    chisquare_value, pvalue_gender_income = chisquare(observed_values, expected_values)
    print(chisquare_value, pvalue_gender_income, sep='\n')


if __name__ == '__main__':
    main()
