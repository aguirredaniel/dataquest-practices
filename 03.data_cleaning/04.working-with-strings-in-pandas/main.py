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


# - Create a regular expression that will match years and assign it to the variable pattern. Note: we've already set up
#   the pattern variable. Insert your answer inside the parantheses: "(your_answer)".
# - Use pattern and the Series.str.extract() method to extract years from the SpecialNotes column. Assign the resulting
#   Series to years.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    world_dev = pd.read_csv('World_dev.csv')

    merged = pd.merge(happiness2015, world_dev, how='left', left_on='Country', right_on='ShortName')
    col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}
    merged.rename(col_renaming, axis=1, inplace=True)

    pattern = r"([1-2][0-9][0-9][0-9])"
    years = merged['SpecialNotes'].str.extract(pattern)
    print(years.head())


if __name__ == '__main__':
    main()
