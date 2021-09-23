import pandas as pd


# - Use the pd.merge() function to combine happiness2015 and world_dev. Save the resulting dataframe to merged. As a
#   reminder, you can use the following syntax to combine the dataframes: pd.merge(left=df1, right=df2, how='left',
#   left_on='left_df_Column_Name', right_on='right_df_Column_Name').
#   - Set the left_on parameter to the Country column from happiness2015 and the right_on parameter to the ShortName
#   column from world_dev.
# - Use the DataFrame.rename() method to rename the SourceOfMostRecentIncomeAndExpenditureData column in merged to
#   IESurvey (because we don't want to keep typing that long name!).
#   - We've already saved the mapping to a dictionary named col_renaming.
#   - Make sure to set the axis parameter to 1.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    world_dev = pd.read_csv('World_dev.csv')

    merged = pd.merge(happiness2015, world_dev, how='left', left_on='Country', right_on='ShortName')
    col_renaming = {'SourceOfMostRecentIncomeAndExpenditureData': 'IESurvey'}
    merged.rename(col_renaming, axis=1, inplace=True)


if __name__ == '__main__':
    pass
