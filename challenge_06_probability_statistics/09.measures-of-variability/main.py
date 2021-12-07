import pandas as pd


def get_range(distribution: []):
    """
    For given array of numerical values, returns the range of that array.
    Args:
        distribution:

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
        distribution:

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
        distribution:

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
        distribution:

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


# - Write a function that takes in a numerical array and returns the average distance (as explained above). Inside the
#   function's definition:
#   - Compute the mean of the array.
#   - Initialize an empty list.
#   - Loop through the values of the array. For each iteration:
#     - Compute the distance between the current value and the mean. Use value - mean every time, as indicated by the
#        formula.
#     - Append the distance to the list we initialized before the loop.
#     - At the end of the loop, the list should contain all the distances.
#   - Return the mean of the list.
#  - Compute the average distance for distribution C using the function you wrote, and assign the result to a variable
#    named avg_distance.
#  - Print the result. Why do you think we got that value? (Hint: The mean is the balance point of a distribution.).
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')
    C = [1, 1, 1, 1, 1, 1, 1, 1, 1, 21]
    variance_C = variance(C)
    print(variance_C)



if __name__ == '__main__':
    main()
