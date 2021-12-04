import pandas as pd


def mode(values: []):
    """
    Takes in an array of values (including strings) and returns the mode of that array.
    Args:
        values: List of values to calculate the mode.

    Returns:
        The mode of given array.

    Examples
    ______
    >>> values = [1, '30', '30', 2, 3, '30']
    >>> mode (values)
    '30'
    """
    frequency_table = {}
    for v in values:
        if v in frequency_table:
            frequency_table[v] = frequency_table[v] + 1
        else:
            frequency_table[v] = 1

    return sorted(frequency_table, key=frequency_table.get)[-1]


# - Write a function that takes in an array of values (including strings) and returns the mode of that array. Inside the
#   function's definition:
#   - Initialize an empty dictionary.
#   - Loop through the values of the array that the function takes in. For each iteration of the loop:
#     - If the value is already a key in the dictionary we initialized before the loop, increment its dictionary value
#       by 1.
#     - Else, define the value as a key in the dictionary, and set the initial dictionary value to 1.
#   - You should end up with a dictionary containing the unique values of the array as dictionary keys and the count for
#     each unique value as a dictionary value: example_dictionary = {'unique_value1': 230, 'unique_value2': 23,
#     'unique_value3': 328}.
#   - Return the key with the highest count (this key is the mode of the array). For instance, for the
#     example_dictionary above, you should return the string unique_value3.
#   - You can use this technique to return the key corresponding to the highest value.
# - Using the function you wrote, measure the mode of the Land Slope variable, and assign the result to a variable
#   named mode_function.
# - Using the Series.mode() method, measure the mode of the Land Slope variable, and assign the result to a
#   variable named mode_method.
# - Compare the two modes using the == operator to check whether they are the same and assign the result of the
#   comparison to a variable named same.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')
    mode_function = mode(houses['Land Slope'])
    mode_method = houses['Land Slope'].mode().iloc[0]
    same = mode_function == mode_method

    assert same


if __name__ == '__main__':
    main()
