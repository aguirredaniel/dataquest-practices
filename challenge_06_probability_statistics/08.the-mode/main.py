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


# - Find the class interval with the highest frequency, then find its midpoint. For instance, the midpoint of the class
#   interval (0, 100000] is 50000.
#   - Assign the midpoint value to a variable named mode. Make sure the value you assign is of the int type.
# - Find the mean of the SalePrice column and assign it to a variable named mean.
# - Find the median of the SalePrice column and assign it to a variable named median.
# - Assess the truth value of the following sentences:
#   - The mode is lower than the median, and the median is lower than the mean.
#     - If you think this is true, assign the boolean True to a variable named sentence_1, otherwise assign False.
#   - The mean is greater than the median, and the median is greater than the mode.
#     - Assign True or False to a variable named sentence_2.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')

    intervals = pd.interval_range(start=0, end=800000, freq=100000)
    gr_freq_table = pd.Series([0, 0, 0, 0, 0, 0, 0, 0], index=intervals)

    for value in houses['SalePrice']:
        for interval in intervals:
            if value in interval:
                gr_freq_table.loc[interval] += 1
                break

    mode = (100000 + 200000) / 2
    mean = houses['SalePrice'].mean()
    median = houses['SalePrice'].median()

    sentence_1 = True
    sentence_2 = True


if __name__ == '__main__':
    main()
