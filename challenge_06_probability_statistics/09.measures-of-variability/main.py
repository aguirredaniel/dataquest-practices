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


# - Use the Series.std() method to compute the sample standard deviation for the SalePrice column. You can use the ddof
#   parameter to choose between n and n − 1. Save the result to a variable named pandas_stdev.
# - Use the numpy.std() function to compute the sample standard deviation for the SalePrice column. You can use the ddof
#   parameter to choose between n and n − 1. Save the result to a variable named numpy_stdev.
# - Compare pandas_stdev with numpy_stdev using the == operator. Assign the result of the comparison to a variable named
#   equal_stdevs.
# - Use the Series.var() method to compute the sample variance for the SalePrice column. Assign the result to pandas_var.
# - Use the numpy.var() function to compute the sample variance for the SalePrice column. Assign the result to numpy_var.
# - Compare pandas_var with numpy_var using the == operator. Assign the result of the comparison to a variable named
#   equal_vars.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')

    sample = houses.sample(100, random_state=1)
    sale = sample['SalePrice']

    pandas_stdev = sale.std(ddof=1)
    numpy_stdev = std(sale, ddof=1)
    equal_stdevs = pandas_stdev == numpy_stdev
    assert equal_stdevs

    pandas_var = sale.var(ddof=1)
    numpy_var = var(sale, ddof=1)
    equal_vars = pandas_var == numpy_var
    assert equal_vars


if __name__ == '__main__':
    main()
