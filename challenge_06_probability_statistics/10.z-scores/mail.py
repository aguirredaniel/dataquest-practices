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


# - Standardize the population of values stored in the population variable and compute its mean  μz and its standard
#    deviation σz .
#   - Assign the value of μz to a variable named mean_z.
#   - Assign the value of σ z to a variable named stdev_z.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')

    population = [0, 8, 0, 8]

    standard_populaiton = [(p - mean(population)) / std(population) for p in population]
    mean_z = mean(standard_populaiton)
    stdev_z = std(standard_populaiton)


if __name__ == '__main__':
    main()
