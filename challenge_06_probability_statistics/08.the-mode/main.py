import pandas as pd


def get_mode(values: []):
    """
    Takes in an array of values (including strings) and returns the mode of that array.
    Args:
        values: List of values to calculate the mode.

    Returns:
        The mode of given array, and the frequency table of all values.

    Examples
    ______
    >>> values = [1, '30', '30', 2, 3, '30']
    >>> mode (values)
    ('30', {1:1, '30': 3, 2:1, 3:1})
    """
    frequency_table = {}
    for v in values:
        if v in frequency_table:
            frequency_table[v] += 1
        else:
            frequency_table[v] = 1

    return max(frequency_table, key=frequency_table.get), frequency_table


# - Explore the Bedroom AbvGr variable, and find whether it's discrete or continuous. You can refer to the documentation
#   for the possible values for this column.
#   - If it's discrete, assign the string 'discrete' to a variable named bedroom_variable, otherwise assign 'continuous'
#   - If it's discrete, compute its mode using Series.mode() and assign the result to a variable named bedroom_mode.
# - Find whether the SalePrice variable is discrete or continuous.
#   - If it's discrete, assign the string 'discrete' to a variable named price_variable, otherwise assign 'continuous'.
#   -If it's discrete, compute its mode using Series.mode() and assign the result to a variable named price_mode.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')

    print(houses['Bedroom AbvGr'].unique())
    print(houses['SalePrice'].unique())

    bedroom_variable = 'discrete'
    bedroom_mode = houses['Bedroom AbvGr'].mode()
    price_variable = 'continuous'

    print(bedroom_mode)


if __name__ == '__main__':
    main()
