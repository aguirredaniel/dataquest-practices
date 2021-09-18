import pandas as pd


# - Use the pandas.read_csv() function to read the World_Happiness_2016.csv file into a dataframe called happiness2016
#   and the World_Happiness_2017.csv file into a dataframe called happiness2017.
# - Add a column called Year to each dataframe with the corresponding year. For example, the Year column in
#   happiness2015 should contain the value 2015 for each row.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    happiness2016 = pd.read_csv('World_Happiness_2016.csv')
    happiness2017 = pd.read_csv('World_Happiness_2017.csv')

    happiness2015['Year'] = 2015
    happiness2016['Year'] = 2016
    happiness2017['Year'] = 2017


if __name__ == '__main__':
    main()
