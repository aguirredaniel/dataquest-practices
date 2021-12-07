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


# - Write a function that takes in a numerical array and returns the standard deviation of that array. Inside the
#   function:
#   - Compute the mean of the array.
#   - Loop through the values of the array. For each iteration:
#     - Compute the squared distance (squared deviation).
#     - Append the squared distance to a list.
#  - Compute the mean of the list of squared distances — this is the variance.
#  - Return the square root of the variance.
# - Compute the standard deviation of distribution C, and assign the result to a variable named standard_deviation_C.
# - Is the result considerably less than 20 but greater than 0, as we expected?
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')
    C = [1, 1, 1, 1, 1, 1, 1, 1, 1, 21]
    standard_deviation_C = standard_deviation(C)
    print(standard_deviation_C)


if __name__ == '__main__':
    main()
