import pandas as pd


def mean(distribution):
    return sum(distribution) / len(distribution)


# - Use the function you wrote in step 5 to compute the mean of the SalePrice distribution. Assign the result to a
#   variable named function_mean.
# - Use Series.mean() to compute the mean of the SalePrice distribution. Assign the result to a variable named
#   pandas_mean.
# - Compare function_mean with pandas_mean using the == operator. Assign the result of the comparison to a variable
#   named means_are_equal.
#   - The two means should be equal, so we expect the comparison to resolve to True
def main():
    houses = pd.read_csv('AmesHousing_1.txt', sep='\t')
    function_mean = mean(houses['SalePrice'])
    pandas_mean = houses['SalePrice'].mean()

    means_are_equal = function_mean == pandas_mean


if __name__ == '__main__':
    main()
