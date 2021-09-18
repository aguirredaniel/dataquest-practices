import pandas as pd


# - Update merged to use the suffixes _2015 and _2016. Set the suffixes parameter to ('_2015', '_2016') in merge().
#   Assign the result to merged_suffixes.
# - Update merged_updated to use the suffixes _2015 and _2016. Notice that the "left" dataframe is three_2016 and the
#   "right" dataframe is three_2015. Assign the result to merged_updated_suffixes.
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

    merged = pd.merge(left=three_2015, right=three_2016, how='left', on='Country')
    merged_updated = pd.merge(left=three_2016, right=three_2015, how='left', on='Country')

    merged_suffixes = pd.merge(left=three_2015, right=three_2016,
                               how='left', on='Country',
                               suffixes=('_2015', '_2016'))
    merged_updated_suffixes = pd.merge(left=three_2016, right=three_2015,
                                       how='left', on='Country',
                                       suffixes=('_2016', '_2015'))

if __name__ == '__main__':
    main()
