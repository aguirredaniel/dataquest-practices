import pandas as pd


# - Use the pd.merge() function to join three_2015 and three_2016 on the Country column. Assign the result to merged.
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


if __name__ == '__main__':
    main()
