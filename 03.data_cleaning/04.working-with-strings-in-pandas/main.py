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


# - Use the Series.str.split() method to split the CurrencyUnit column into a list of words and then use the
#   Series.str.get() method to select just the last word. Assign the result to merged['Currency Vectorized'].
# - Use the Series.head() method to print the first five rows in merged['Currency Vectorized'].
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    world_dev = pd.read_csv('World_dev.csv')

    merged = pd.merge(happiness2015, world_dev, how='left', left_on='Country', right_on='ShortName')
    col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}
    merged.rename(col_renaming, axis=1, inplace=True)

    merged['Currency Vectorized'] = merged['CurrencyUnit'].str.split().str.get(-1)
    print(merged['Currency Vectorized'].head())


if __name__ == '__main__':
    main()
