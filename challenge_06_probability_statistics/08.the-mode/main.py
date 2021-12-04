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


# - In the code editor you can see the mean, mode and median for three distributions. Indicate whether the mean, median,
#   and mode of each distribution suggest a left or a right skew.
#   - If the values for distribution_1 indicate a right skew, assign the string 'right skew' to a variable named
#     shape_1, otherwise assign 'left skew'.
#   - If the values for distribution_2 indicate a right skew, assign the string 'right skew' to a variable named
#     shape_2, otherwise assign 'left skew'.
#   - If the values for distribution_3 indicate a right skew, assign the string 'right skew' to a variable named
#     shape_3, otherwise assign 'left skew'.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')

    distribution_1 = {'mean': 3021, 'median': 3001, 'mode': 2947}
    distribution_2 = {'median': 924, 'mode': 832, 'mean': 962}
    distribution_3 = {'mode': 202, 'mean': 143, 'median': 199}

    shape_1 = 'right skew'
    shape_2 = 'right skew'
    shape_3 = 'left skew'


if __name__ == '__main__':
    main()
