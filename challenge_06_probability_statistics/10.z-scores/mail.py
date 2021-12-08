import matplotlib.pyplot as plt
import pandas as pd
from numpy import mean, std


def z_score(distribution: [], value, bessel=0) -> float:
    """
        Calculate the Z score of value in distributions that belongs.
    Args:
        distribution: array of numerically values.
        value: value that  belongs to distribution array.
        bessel: Bassel's correction for standard deviation.

    Returns:
        Float value, represent how far off a value is from the mean in terms of number of standard deviations.

    Examples
    ______
    >>> distribution = [30, 19, 10]
    >>> z_score(distribution, 30)
    1.2634656762057945
    """

    return (value - mean(distribution)) / std(distribution, ddof=bessel)


# - Compute the standard deviation of standardized_sample using the sample standard deviation formula, and assign the
#   result to a variable named stdev_sample.
# - Inspect the result to see if the standard deviation equals 1.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')

    population = [0, 8, 0, 8]

    standardized_sample = [(p - mean(population)) / std(population, ddof=1) for p in population]
    stdev_sample = std(standardized_sample, ddof=1)

    print(stdev_sample)


if __name__ == '__main__':
    main()
