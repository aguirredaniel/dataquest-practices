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


# - Use the Series.str.extractall() method to extract pattern from the IESurvey column. Assign the result to years.
# - Use vectorized slicing to extract the first two numbers from the First_Year column in years (For example, extract
#   "20" from "2000"). Assign the result to first_two_year.
# - Add first_two_year to the Second_Year column in years, so that Second_Year contains the full year (ex: "2000").
#   Assign the result to years['Second_Year'].
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    world_dev = pd.read_csv('World_dev.csv')

    merged = pd.merge(happiness2015, world_dev, how='left', left_on='Country', right_on='ShortName')
    col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}
    merged.rename(col_renaming, axis=1, inplace=True)

    merged = merged.set_index('Country')
    pattern = r"(?P<First_Year>[1-2][0-9]{3})/?(?P<Second_Year>[0-9]{2})?"
    years = merged['IESurvey'].str.extractall(pattern)
    first_two_year = years['First_Year'].str[:2]
    years['Second_Year'] = first_two_year.str.cat(years['Second_Year'])

    print(years.sort_values('Second_Year').head())


if __name__ == '__main__':
    main()
