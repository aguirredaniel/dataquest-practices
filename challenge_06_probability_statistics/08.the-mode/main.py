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


# - Edit the function you wrote to return both the mode of an array and the dictionary containing the count for each
#   unique value in the array.
# - Use the edited function to return, at the same time, the mode of the Roof Style variable and the dictionary
#   containing the counts for each unique value.
#   - Assign the mode to a variable named mode.
#   - Assign the dictionary to a variable named value_counts.
# - Inspect the content of value_counts and compare it to the value count we'd get by using the Series.value_counts()
#   method.
#   - This exercise is meant to give you a better understanding of what happens under the hood when we run
#     Series.value_counts().
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')
    mode, value_counts = get_mode(houses['Roof Style'])
    value_counts_method = houses['Roof Style'].value_counts()

    assert value_counts == dict(value_counts_method)


if __name__ == '__main__':
    main()
