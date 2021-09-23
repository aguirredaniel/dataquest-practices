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


# - Use the Series.str.len() method to return the length of each element in the CurrencyUnit column. Assign the result
#   to lengths.
# - Use the Series.value_counts() method to return the count of unique values in lengths. Set the dropna parameter to
#   False so NaNs are counted, too. Assign the result to value_counts.
#   - If value_counts contains NaNs, it means the Series.str.len() method excluded them and didn't treat them as strings.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    world_dev = pd.read_csv('World_dev.csv')

    merged = pd.merge(happiness2015, world_dev, how='left', left_on='Country', right_on='ShortName')
    col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}
    merged.rename(col_renaming, axis=1, inplace=True)

    lengths = merged['CurrencyUnit'].str.len()
    value_counts = lengths.value_counts(dropna=False)
    print(lengths, value_counts, sep='\n')


if __name__ == '__main__':
    main()
