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


# - We've already transformed the distribution of the SalePrice variable to distribution of z-scores and saved the new
#   values to a column named z_prices.
#   - Compute the mean of the z_prices column and assign the result to a variable named z_mean_price.
#   - Compute the standard deviation of the z_prices column and assign the result to a variable named z_stdev_price.
#     Assume that you're computing the standard deviation for a population.
# - Transform the distribution of the Lot Area variable into a distribution of z-scores.
#   - Compute the mean of the new distribution of z-scores and assign the result to a variable named z_mean_area.
#   - Compute the standard deviation of the new distribution of z-scores and assign the result to a variable named
#     z_stdev_area. Assume that you're computing the standard deviation for a population.
# - Compare the values of z_mean_price and z_mean_area. What do you observe? How can you explain that?
# - Compare the values of z_stdev_price and z_stdev_area. What do you observe? How can you explain that?
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')

    sale = houses['SalePrice']
    houses['z_prices'] = sale.apply(lambda v: z_score(sale, v))
    z_mean_price = houses['z_prices'].mean()
    z_stdev_price = houses['z_prices'].std(ddof=0)

    area = houses['Lot Area']
    houses['z_area'] = area.apply(lambda v: z_score(area, v))
    z_mean_area = houses['z_area'].mean()
    z_stdev_area = houses['z_area'].std(ddof=0)


if __name__ == '__main__':
    main()
