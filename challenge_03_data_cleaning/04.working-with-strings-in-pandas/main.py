import pandas as pd
import matplotlib.pyplot as plt


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


# - Use some of the string methods above to clean the IncomeGroup column.
#   - Make sure to remove the whitespace at the end of the strings.
# - Use the df.pivot_table() method to return the mean of each income group in the IncomeGroup column. Set the index
#   parameter equal to the IncomeGroup column and the values parameter equal to the Happiness Score column. Assign the
#   result to pv_incomes.
# - Use the df.plot() method to plot the results. Set the kind parameter equal to bar, the rot parameter equal to 30,
#   and the ylim parameter equal to (0,10).
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    world_dev = pd.read_csv('World_dev.csv')

    merged = pd.merge(happiness2015, world_dev, how='left', left_on='Country', right_on='ShortName')
    col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}
    merged.rename(col_renaming, axis=1, inplace=True)

    merged = merged.set_index('Country')
    pattern = r'income:?\s?'
    merged['IncomeGroup'] = merged['IncomeGroup'].str.replace(pattern, '').str.upper().str.strip()
    pv_incomes = pd.pivot_table(merged, index='IncomeGroup', values='Happiness Score')
    pv_incomes.plot(kind='bar', rot=30, ylim=(0, 10))
    plt.show()


if __name__ == '__main__':
    main()
