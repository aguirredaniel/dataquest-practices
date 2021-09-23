import pandas as pd


def extract_last_word(element):
    """
        Slit a string value by empty space and returns the last word.
    Args:
        element:
         A strinig value.
    Returns:
        The last word in string value.

    Examples:
        >>> extract_last_word('Canadian dollar')
        'dollar'
    """
    element_str = str(element)

    return element_str.split()[-1]


# - Write a function called extract_last_word with the following criteria:
# - The function should accept one parameter called element.
# - Use the string.split() method to split the object into a list. First convert element to a string as follows:
#   str(element).
# - Return the last word of the list.
# - Use the Series.apply() method to apply the function to the CurrencyUnit column. Save the result to
#   merged['Currency Apply'].
# - Use the Series.head() method to print the first five rows in merged['Currency Apply'].
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    world_dev = pd.read_csv('World_dev.csv')

    merged = pd.merge(happiness2015, world_dev, how='left', left_on='Country', right_on='ShortName')
    col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}
    merged.rename(col_renaming, axis=1, inplace=True)

    merged['Currency Apply'] = merged['CurrencyUnit'].apply(extract_last_word)
    print(merged['Currency Apply'].head())


if __name__ == '__main__':
    main()
