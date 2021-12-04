import pandas as pd
import matplotlib.pyplot as plt


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
    >>> get_mode(values)
    ('30', {1:1, '30': 3, 2:1, 3:1})
    """
    frequency_table = {}
    for v in values:
        if v in frequency_table:
            frequency_table[v] += 1
        else:
            frequency_table[v] = 1

    return max(frequency_table, key=frequency_table.get), frequency_table


# -
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')

    houses['Mo Sold'].plot.kde(xlim=(
        houses['Mo Sold'].min(), houses['Mo Sold'].max()))
    plt.axvline(houses['Mo Sold'].mode().iloc[0], color='Green', label='Mode')
    plt.axvline(houses['Mo Sold'].median(), color='Orange', label='Median')
    plt.axvline(houses['Mo Sold'].mean(), color='Black', label='Mean')
    plt.legend()
    
    plt.show()


if __name__ == '__main__':
    main()
