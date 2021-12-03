import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def weighted_mean(means, weights) -> float:
    """
        Calculate the weighted mean.
    Args:
        means: Array containing the mean values.
        weights: Array with the corresponding weights for mean values.

    Returns:
        Float value for result of weighted mean.
    Examples
    _______
    >>> means = [181761.648000, 185138.207493, 178841.750804, 181404.567901, 172597.598240]
    >>> weights = [625, 694, 622, 648, 341]
    >>> weighted_mean(means, weights)
    180796.0600682314
    """
    weight = 0
    mean_weight = 0
    for m, w in zip(means, weights):
        mean_weight += m * w
        weight += w

    return mean_weight / weight


# - Find the median value of the TotRms AbvGrd column.
#   - Sort the values in the column in ascending order.
#     - Replace the '10 or more' value with the integer 10 using the Series.replace() method. We do this only for
#       sorting purposes. To avoid modifying the data in the original data set, make a copy of the column using the
#       Series.copy() method and save it to a distinct variable.
#     - Convert the column to the int type using the Series.astype() method.
#     - Sort the values in ascending order using the Series.sort_values() method.
# - Depending on whether the distribution has an odd or even number of values, find the median and assign it to a
#   variable named median.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')

    lot_area = houses['Lot Area']
    lot_area.plot.box()
    plt.show()

    sale_price = houses['SalePrice']
    sale_price.plot.box()
    plt.show()

    lotarea_difference = lot_area.mean() - lot_area.median()
    saleprice_difference = sale_price.mean() - sale_price.median()

    print(lotarea_difference, saleprice_difference, sep='\n')


if __name__ == '__main__':
    main()
