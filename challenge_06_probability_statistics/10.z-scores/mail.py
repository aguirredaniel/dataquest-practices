import matplotlib.pyplot as plt
import pandas as pd
from numpy import mean, std


def z_score(distribution: [], value, bessel=0) -> float:
    """
        Calculate the Z score of value in distributions that belongs.
    Args:
        distribution: array of numerically values.
        value: value that  belongs to distribution array.
        bessel: Bassel's correction for standard deviation.

    Returns:
        Float value, represent how far off a value is from the mean in terms of number of standard deviations.

    Examples
    ______
    >>> distribution = [30, 19, 10]
    >>> z_score(distribution, 30)
    1.2634656762057945
    """

    return (value - mean(distribution)) / std(distribution, ddof=bessel)


# - Standardize the distributions of the index_1 and index_2 variables. We've coded these columns under the hood, and
#   they're already part of the houses data set.
#  - Assume that the values we have for both variables constitute populations.
#  - Don't forget that each distribution has its own mean and standard deviation.
# - Print the z-scores for the first two houses in the data set to find out which house has a better overall quality.
#   - Assign your answer as a string to a variable named better — if the first house is better, assign 'first',
#     otherwise assign 'second'.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')
    houses['z_index_1'] = houses['index_1'].apply(lambda v: (v - houses['index_1'].mean()) / houses['index_1'].std())
    houses['z_index_2'] = houses['index_2'].apply(lambda v: (v - houses['index_2'].mean()) / houses['index_2'].std())
    print(houses[['z_index_1', 'index_2']].iloc[:2])
    better = 'first'


if __name__ == '__main__':
    main()
