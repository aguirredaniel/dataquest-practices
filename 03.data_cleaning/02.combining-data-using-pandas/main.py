import pandas as pd


# - Update merged to use a left join instead of an inner join. Set the how parameter to 'left' in merge(). Assign the
#   result to merged_left.
# - Update merged_left so that the left parameter equals three_2016 and the right parameter equals three_2015. Assign
#   the result to merged_left_updated.
# - Based on the results of this exercise, when using a left join, does changing the dataframe assigned to the left and
#   right parameters change the result? Try to answer this question before moving onto the next screen.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    happiness2016 = pd.read_csv('World_Happiness_2016.csv')
    happiness2017 = pd.read_csv('World_Happiness_2017.csv')

    # Adding corresponding 'Year' column
    happiness2015['Year'] = 2015
    happiness2016['Year'] = 2016
    happiness2017['Year'] = 2017

    three_2015 = happiness2015[['Country', 'Happiness Rank', 'Year']].iloc[2:5]
    three_2016 = happiness2016[['Country', 'Happiness Rank', 'Year']].iloc[2:5]

    merged = pd.merge(left=three_2015, right=three_2016, on='Country')
    merged_left = pd.merge(left=three_2015, right=three_2016, on='Country', how='left')
    merged_left_updated = pd.merge(left=three_2016, right=three_2015, on='Country', how='left')


if __name__ == '__main__':
    main()
