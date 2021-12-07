import pandas as pd
from math import sqrt
import matplotlib.pyplot as plt


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


# - We took two samples of 50 sample points each from the distribution of the Year Built variable. Examine the graph
#   below, and estimate visually which sample has a bigger spread.
#   - Assign your answer to a variable named bigger_spread. If you think sample 1 has a bigger spread, assign the string
#    'sample 1' to bigger_spread, otherwise assign 'sample 2'.
#   - Sanity check your visual estimate by computing and comparing the standard deviations of the two samples.
#     - You can see the two samples already saved in the code editor.
#     - Assign the standard deviation of sample 1 to a variable named st_dev1. Compute the standard deviation using the
#       standard_deviation() function.
#     - Assign the standard deviation of sample 2 to a variable named st_dev2. Compute the standard deviation using the
#       standard_deviation() function.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')
    sample1 = houses['Year Built'].sample(50, random_state=1)
    sample2 = houses['Year Built'].sample(50, random_state=2)

    st_dev1 = standard_deviation(sample1)
    st_dev2 = standard_deviation(sample2)
    print(st_dev1, st_dev2, sep='\n')
    bigger_spread = 'sample 2'

    sample1.plot.hist()
    plt.show()
    sample2.plot.hist()
    plt.show()


if __name__ == '__main__':
    main()
