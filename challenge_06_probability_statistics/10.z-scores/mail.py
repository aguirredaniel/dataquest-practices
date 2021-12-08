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


# - We merged the two columns of z-scores together into a new column named z_merged.
#  - Transform the standardized distribution of z_merged to a distribution with a μ = 50 and σ = 10 using the formula
#    x = zσ + μ.
# - Compute the mean of the newly transformed distribution — the mean should be 50, but expect some minor rounding
#   errors.
#   - Assign the result to a variable named mean_transformed.
# - Compute the standard deviation of the newly transformed distribution — the standard deviation should be 10, but
#   expect some minor rounding errors.
#   - Assign the result to a variable named stdev_transformed.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')
    houses['z_merged'] = houses['z_merged'].apply(lambda z: z * 10 + 50)
    mean_transformed = houses['z_merged'].mean()
    stdev_transformed = houses['z_merged'].std(ddof=0)

if __name__ == '__main__':
    main()
