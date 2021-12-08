import matplotlib.pyplot as plt
import pandas as pd
from numpy import mean, std


def z_score(distribution: [], value) -> float:
    """
        Calculate the Z score of value in distributions that belongs.
    Args:
        distribution: array of numerically values.
        value: value that  belongs to distribution array.

    Returns:
        Float value, represent how far off a value is from the mean in terms of number of standard deviations.

    Examples
    ______
    >>> distribution = [30, 19, 10]
    >>> z_score(distribution, 30)
    1.2634656762057945
    """

    return (value - mean(distribution)) / std(distribution)


# - Write a function that takes in a value, the array the value belongs to, and returns the z-score of that value.
#   Inside the function's definition:
#   - Compute the mean of the array.
#   - Compute the standard deviation of the array. Make sure your function is flexible enough to compute z-scores for
#     both samples and populations.
#     - You can use the std() function from numpy.
#   - Find out the distance between the value and the mean of the array.
#   - Compute the z-score by dividing the distance to the standard deviation of the array.
#   - Return the z-score.
# - Compute the z-score for min_val, mean_val, max_val, which are already defined in the code editor. Assume that the
#   values come from a population.
#   - Assign the z-score for min_val to a variable named min_z.
#   -Assign the z-score for mean_val to a variable named mean_z.
#   - Assign the z-score for max_val to a variable named max_z.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')

    sale = houses['SalePrice']
    min_z = z_score(sale, sale.min())
    mean_z = z_score(sale, sale.mean())
    max_z = z_score(sale, sale.max())

    print(min_z, mean_z, max_z, sep='\n')


if __name__ == '__main__':
    main()
