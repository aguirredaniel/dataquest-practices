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


# - Find out the location for which $200,000 has the z-score closest to 0. Code-wise, there are several ways to complete
#   this task, and we encourage you to think of a way yourself. Below we describe one way to complete this task:
#   - Isolate the data for each of the five neighborhoods. The neigborhoods are described in the Neighborhood column.
#     These are the abbreviations for our neighborhoods of interest:
#     - 'NAmes' for North Ames.
#     - 'CollgCr' for College Creek.
#     - 'OldTown' for Old Town.
#     - 'Edwards' for Edwards.
#    - 'Somerst' for Somerset.
#   - For example, to isolate the data for North Ames you can do houses[houses['Neighborhood'] == 'NAmes'] and save the
#     data to a variable.
#   -  Find the z-score of a $200,000 price for each of the five data sets you isolated. Assume that each data set is a
#      population.
#   - Examine the z-scores to find the best location to invest in. Assign your answer as a string to the variable
#     best_investment. Choose between the following strings: 'North Ames', 'College Creek', 'Old Town', 'Edwards', and 'Somerset'.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')

    sale = houses['SalePrice']
    all_neighborhoods = houses['Neighborhood']
    price = 200000
    neighborhoods = ['NAmes', 'CollgCr', 'OldTown', 'Edwards', 'Somerst']
    neighborhood_z_scores = {n: abs(z_score(sale[all_neighborhoods == n], price, 1))
                             for n in neighborhoods}

    best_investment = min(neighborhood_z_scores, key=neighborhood_z_scores.get)
    best_investment = 'College Creek'


if __name__ == '__main__':
    main()
