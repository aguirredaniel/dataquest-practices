import pandas as pd
from math import sqrt


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

    return squared_distances / len(distribution)


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


# - The standard deviation of the SalePrice variable should give us a picture about the diversity of prices on the real
#   estate market.
#   - Find the year with the greatest variability of prices and assign the answer as an integer to the variable
#     greatest_variability.
#   - Find the year with the lowest variability of prices and assign the answer as an integer to the variable
#     lowest_variability.
#   - Use the function you wrote in the previous screen to measure the standard deviation of each year.
#   - You can find information about the years of sale in the Yr Sold column.
#   - There are many ways you can solve this exercise. If you get stuck, you can check the hint or the solution code.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')
    years = houses['Yr Sold'].unique()
    sales = houses['SalePrice']
    variability_by_year = {year: standard_deviation(sales[houses['Yr Sold'] == year]) for year in years}

    greatest_variability = max(variability_by_year, key=variability_by_year.get)
    lowest_variability = min(variability_by_year, key=variability_by_year.get)

    print(greatest_variability, lowest_variability, sep='\n')


if __name__ == '__main__':
    main()
