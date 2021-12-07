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


# - Let's consider the data we have for SalePrice a population and sample it 5000 times. For each of the 5000 iterations
#   of a for loop:
#   - Sample 10 data points from the SalePrice variable using the Series.sample() method.
#     - The random_state of Series.sample() should be 0 for the first iteration, 1 for the second iteration, 2 for the
#       third, and so on.
#   - Compute the standard deviation of the sample using the standard_deviation() function.
#   - Append the standard deviation to a list that will eventually store all the 5000 sample standard deviations.
# - Generate a histogram using plt.hist() to visualize the distribution of the 5000 sample standard deviations.
# - Draw a vertical line using plt.axvline() to mark the population standard deviation.
# - Examine the histogram and try to figure out whether most sample standard deviations cluster above or below the
#   population standard deviation, or right at the center of it.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')
    sales = houses['SalePrice']
    parameter = standard_deviation(sales)
    standard_deviations = [standard_deviation(sales.sample(10, random_state=i))
                           for i in range(5000)]

    plt.hist(standard_deviations)
    plt.axvline(parameter)

    plt.show()


if __name__ == '__main__':
    main()
