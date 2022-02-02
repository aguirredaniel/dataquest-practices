import numpy as np
from scipy.stats import chisquare


# - Use the scipy.stats.chisquare function to calculate the p-value for the following table:
# - Assign the result to race_pvalue.
def chi_squared(observed, expected):
    return (observed - expected) ** 2 / expected


def main():
    observed = np.array([27816, 3124, 1039, 311, 271, ])
    expected = np.array([26146.5, 3939.9, 944.3, 260.5, 1269.8])

    race_chisq, race_pvalue = chisquare(observed, expected)

    print(race_chisq, race_pvalue, sep='\n')


if __name__ == '__main__':
    main()
