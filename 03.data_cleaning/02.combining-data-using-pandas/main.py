import pandas as pd


# - Predict the number of rows and columns the resulting dataframe will have. Assign the number of rows to a variable
#   called rows and the number of columns to a variable called columns.
# - To change the join type used in merge_index to a left join, set the how parameter equal to 'left'. Save the result
#   to merge_index_left.
# - Update rows and columns so that each contains the correct number of rows and columns in merge_index_left.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    happiness2016 = pd.read_csv('World_Happiness_2016.csv')
    happiness2017 = pd.read_csv('World_Happiness_2017.csv')

    # Adding corresponding 'Year' column
    happiness2015['Year'] = 2015
    happiness2016['Year'] = 2016
    happiness2017['Year'] = 2017

    four_2015 = happiness2015[['Country', 'Happiness Rank', 'Year']].iloc[2:6]
    three_2016 = happiness2016[['Country', 'Happiness Rank', 'Year']].iloc[2:5]
    merge_index = pd.merge(left=four_2015, right=three_2016, left_index=True, right_index=True,
                           suffixes=('_2015', '_2016'))

    merge_index_left = pd.merge(left=four_2015, right=three_2016, how='left', left_index=True, right_index=True,
                                suffixes=('_2015', '_2016'))
    rows = 4
    columns = 6


if __name__ == '__main__':
    main()
