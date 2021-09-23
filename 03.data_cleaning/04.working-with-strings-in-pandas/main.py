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


# - Use the Series.str.extractall() method to extract all of the years in the IESurvey. Assign the result to years.
# - Use the Series.value_counts() method to create a list of the unique years, along with the count. Assign the result
#   to value_counts. Print value_counts.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    world_dev = pd.read_csv('World_dev.csv')

    merged = pd.merge(happiness2015, world_dev, how='left', left_on='Country', right_on='ShortName')
    col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}
    merged.rename(col_renaming, axis=1, inplace=True)

    merged = merged.set_index('Country')
    pattern = r"(?P<Years>[1-2][0-9]{3})"
    years = merged['IESurvey'].str.extractall(pattern)
    value_counts = years['Years'].value_counts()
    print(value_counts)


if __name__ == '__main__':
    main()
