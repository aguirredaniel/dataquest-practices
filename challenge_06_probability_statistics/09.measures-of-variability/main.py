import pandas as pd
from math import sqrt
import matplotlib.pyplot as plt
from numpy import std, var


def get_range(distribution: []):
    """
    For given array of numerical values, returns the range of that array.
    Args:
        distribution: Numerical array

    Returns:
        A numerical value represent a range of distribution.

    Examples
    ------
    >>> distribution = [30,19,10]
    >>> get_range(distribution)
    11
    """
    return max(distribution) - min(distribution)


def average_distance(distribution: []):
    """
    For given numerical array returns the average distance.
    Args:
        distribution: Numerical array


    Returns:
        A numerical value represent the average distance of distribution.

    Examples
    _______
    >>> distribution = [30,19,10]
    >>> average_distance(distribution)
    -1.1842378929335002e-15
    """
    mean = sum(distribution) / len(distribution)
    distances = sum((v - mean for v in distribution))

    return distances / len(distribution)


def mean_absolute_deviation(distribution: []):
    """
    For given numerical array returns the mean absolute deviation.
    Args:
        distribution: Numerical array

    Returns:
        A numerical value represent the mean absolute deviation of distribution.

    Examples
    _______
    >>> distribution = [30,19,10]
    >>> mean_absolute_deviation(distribution)
    6.888888888888889
    """
    mean = sum(distribution) / len(distribution)
    absolute_distances = sum((abs(v - mean) for v in distribution))

    return absolute_distances / len(distribution)


def variance(distribution: []):
    """
    For given numerical array returns the variance.
    Args:
        distribution: Numerical array

    Returns:
        A numerical value represent the variance of distribution.

    Examples
    _______
    >>> distribution = [30,19,10]
    >>> variance(distribution)
    66.8888888888889
    """
    mean = sum(distribution) / len(distribution)
    squared_distances = sum((pow(v - mean, 2) for v in distribution))

    return squared_distances / (len(distribution) - 1)


def standard_deviation(distribution: []):
    """
     For given numerical array returns the standard deviation.
     Args:
         distribution: Numerical array
     Returns:
         A numerical value represent the standard deviation of distribution.

     Examples
     _______
     >>> distribution = [30,19,10]
     >>> standard_deviation(distribution)
     8.178562764256865
     """
    return sqrt(variance(distribution))


# - Compute the sample variance and sample standard deviation for each sample.
#   - Take the mean of all the sample variances. Compare the mean variance with the population variance (which you'll
#     have to compute) using the == operator, and assign the result to a variable equal_var.
#   - If the sample variance is biased in this case, the result should be False.
# - Take the mean of all the sample standard deviations. Compare the mean standard deviation with the population
#   standard deviation using the == operator, and assign the result to equal_stdev.
#   - If the sample variance is biased in this case, the result should be False.
#   equal_vars.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')

    population = [0, 3, 6]

    samples = [[0, 3], [0, 6],
               [3, 0], [3, 6],
               [6, 0], [6, 3]
               ]

    variances = [var(sample, ddof=1) for sample in samples]
    mean_variances = sum(variances) / len(variances)
    population_variance = var(population)
    equal_var = mean_variances == population_variance

    standard_deviations = [std(sample, ddof=1) for sample in samples]

    mean_standard_deviations = sum(standard_deviations) / len(standard_deviations)
    population_standard_deviation = std(population)
    equal_stdev = mean_standard_deviations == population_standard_deviation


if __name__ == '__main__':
    main()
