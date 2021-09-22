import pandas as pd


# - Use the DataFrame.rename() method to change the 'Economy (GDP per Capita)', 'Health (Life Expectancy)', and 'Trust
#   (Government Corruption)' column names to the names specified in the mapping dictionary.
# - Pass the mapping dictionary into the df.rename() method and set the axis parameter to 1.
# - Assign the result back to happiness2015.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    mapping = {'Economy (GDP per Capita)': 'Economy', 'Health (Life Expectancy)': 'Health',
               'Trust (Government Corruption)': 'Trust'}
    happiness2015 = happiness2015.rename(mapping, axis=1)


if __name__ == '__main__':
    main()
