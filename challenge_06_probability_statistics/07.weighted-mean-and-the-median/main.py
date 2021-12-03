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


# - Write a function that computes the weighted mean for any array of numbers.
#   - The function should take in two arrays: one array containing the mean values, and another array with the
#     corresponding weights.
#   - The function returns the weighted mean.
# - Use the function you wrote to compute the weighted mean for the Mean Price column in the houses_per_year data set.
#   Assign the result to a variable named weighted_mean_function.
# - Use the numpy.average() function to compute the weighted mean for the same Mean Price column. Read the documentation
#   to figure out how you can pass in the weights. Assign the result to a variable named weighted_mean_numpy.
# - Compare the two weighted means (the one from your function and the one from np.average()) using the == operator.
#   Round each mean to 10 decimal places to get rid of minor rounding errors. Assign the result to a variable named
#   equal.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')
    houses_per_year_data = {
        'Year': [2006, 2007, 2008, 2009, 2010],
        'Mean Price': [181761.648000, 185138.207493, 178841.750804, 181404.567901, 172597.598240],
        'Houses Sold': [625, 694, 622, 648, 341]
    }

    houses_per_year = pd.DataFrame(houses_per_year_data)
    weighted_mean_function = weighted_mean(houses_per_year['Mean Price'], houses_per_year['Houses Sold'])
    weighted_mean_numpy = np.average(houses_per_year['Mean Price'], weights=houses_per_year['Houses Sold'])
    equal = round(weighted_mean_function) == round(weighted_mean_numpy)
    assert equal


if __name__ == '__main__':
    main()
