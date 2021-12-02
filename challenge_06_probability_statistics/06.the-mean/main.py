from numpy.random import randint, seed


def mean(distribution: [int]) -> float:
    """
    Calculate a mean value for given distributions of values.
    Args:
        distribution: list of int values represent a distribution.

    Returns:
        The mean of distribution

    Examples
    -----------
    >>> values = [42, 24, 32, 11]
    >>> mean(values)
    27.25
    """
    sum_distribution = 0
    n = len(distribution)
    for i in range(n):
        sum_distribution += distribution[i]

    return sum_distribution / n


# - Write a  function takes in an array of numbers and returns its mean value.
# - Use the function you wrote to compute the mean of the three distributions we already defined in the code editor:
#   - For the distribution in distribution_1 assign the mean to a variable named mean_1.
#   - For the distribution in distribution_2 assign the mean to a variable named mean_2.
#   - For the distribution in distribution_3 assign the mean to a variable named mean_3.
def main():
    distribution_1 = [42, 24, 32, 11]
    distribution_2 = [102, 32, 74, 15, 38, 45, 22]
    distribution_3 = [3, 12, 7, 2, 15, 1, 21]

    mean_1 = mean(distribution_1)
    mean_2 = mean(distribution_2)
    mean_3 = mean(distribution_3)

    print(mean_1, mean_2, mean_3, sep='\n')


if __name__ == '__main__':
    main()
