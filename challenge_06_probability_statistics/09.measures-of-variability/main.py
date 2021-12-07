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


# - Using the function you wrote, measure the range of the SalePrice variable for each year of sales. You can find the
#   year of sale in the Yr Sold column.
#   - Store the measures in a dictionary named range_by_year. The keys should be the individual years, and the
#     dictionary values should be the ranges. This is how the dictionary should look like: {2010: 598868, 2009: 575100,
#     2008: 601900,...}.
# - Using the measures of variability you got, assess the truth value of the following sentences:
#   - Prices had the greatest variability in 2008.
#     - If you consider this sentence true, assign the boolean True to a variable named one, otherwise assign False.
#   - Prices variability had a peak in 2007, then the variability started to decrease until 2010 when there was a short
#     increase in variability compared to the previous year (2009).
#     - If you consider this sentence true, assign the boolean True to a variable named two, otherwise assign False.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')
    range_by_year = {year: get_range(houses[houses['Yr Sold'] == year]['SalePrice'])
                     for year in houses['Yr Sold'].unique()}

    print(range_by_year)
    one = False
    two = True


if __name__ == '__main__':
    main()
