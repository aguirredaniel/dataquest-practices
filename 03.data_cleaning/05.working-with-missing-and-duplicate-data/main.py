import pandas as pd


# - Update the columns names for happiness2015 and happiness2016 to match the formatting of the column names in
#   happiness2017. Use the following criteria to rename the columns:
#   - All letters should be uppercase.
#   - There should be only one space between words.
#   - There should be no parentheses in column names
#   - For example, the Health (Life Expectancy) columns should both be renamed to HEALTH LIFE EXPECTANCY.
# - Use the pd.concat() function to combine happiness2015, happiness2016, and happiness2017. Set the
#   ignore_index argument equal to True to reset the index in the resulting dataframe. Assign the result to combined.
# - Use the DataFrame.isnull() and DataFrame.sum() methods to check for missing values. Assign the result to a variable
#   named missing.
def main():
    happiness2015 = pd.read_csv('wh_2015.csv')
    happiness2016 = pd.read_csv('wh_2016.csv')
    happiness2017 = pd.read_csv('wh_2017.csv')

    happiness2015.columns = happiness2015.columns \
        .str.replace(r'[\(*\)]', '') \
        .str.replace(r'\s+', ' ') \
        .str.strip().str.upper()

    happiness2016.columns = happiness2016.columns \
        .str.replace(r'[\(*\)]', '') \
        .str.replace(r'\s+', ' ') \
        .str.strip().str.upper()
    happiness2017.columns = happiness2017.columns.str.replace('.', ' ').str.replace('\s+', ' ').str.strip().str.upper()

    combined = pd.concat([happiness2015, happiness2016, happiness2017], ignore_index=True)
    missing = combined.isnull().sum()
    print(missing)


if __name__ == '__main__':
    main()
