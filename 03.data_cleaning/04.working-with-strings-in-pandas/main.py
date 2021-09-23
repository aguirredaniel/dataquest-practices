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


# - Use the Series.str.contains() method to search for pattern in the SpecialNotes column again. This time, also pass in
#   the na parameter and set it to False. Assign the result to national_accounts.
# - Use national_accounts to index merged, so that only rows that contain "national accounts" or "National accounts" in
#   the SpecialNotes column are returned. Assign the result to merged_national_accounts.
# - Use the DataFrame.head() method to print the first five rows in merged_national_accounts.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    world_dev = pd.read_csv('World_dev.csv')

    merged = pd.merge(happiness2015, world_dev, how='left', left_on='Country', right_on='ShortName')
    col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}
    merged.rename(col_renaming, axis=1, inplace=True)

    pattern = r"[Nn]ational accounts"
    national_accounts = merged['SpecialNotes'].str.contains(pattern, na=False)
    merged_national_accounts = merged[national_accounts]
    print(merged_national_accounts.head())


if __name__ == '__main__':
    main()
