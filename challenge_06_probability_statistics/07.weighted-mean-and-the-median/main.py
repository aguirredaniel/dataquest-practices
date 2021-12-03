import numpy as np
import pandas as pd


def weighted_mean(means, weights) -> float:
    """
        Calculate the weighted mean.
    Args:
        means: Array containing the mean values.
        weights: Array with the corresponding weights for mean values.

    Returns:
        Float value for result of weighted mean.
    Examples
    _______
    >>> means = [181761.648000, 185138.207493, 178841.750804, 181404.567901, 172597.598240]
    >>> weights = [625, 694, 622, 648, 341]
    >>> weighted_mean(means, weights)
    180796.0600682314
    """
    weight = 0
    mean_weight = 0
    for m, w in zip(means, weights):
        mean_weight += m * w
        weight += w

    return mean_weight / weight


# - Compute the median for each of the three distributions we already defined in the code editor.
#   - Assign the median of distribution1 to a variable named median1.
#   - Assign the median of distribution2 to a variable named median2.
#   - Assign the median of distribution3 to a variable named median3.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')
    houses_per_year_data = {
        'Year': [2006, 2007, 2008, 2009, 2010],
        'Mean Price': [181761.648000, 185138.207493, 178841.750804, 181404.567901, 172597.598240],
        'Houses Sold': [625, 694, 622, 648, 341]
    }
    houses_per_year = pd.DataFrame(houses_per_year_data)

    distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
    distribution2 = [55, 38, 123, 40, 71]
    distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']

    median1 = 23
    median2 = 55
    median3 = 32


if __name__ == '__main__':
    main()
