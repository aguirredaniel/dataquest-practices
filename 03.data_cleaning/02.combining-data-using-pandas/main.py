import pandas as pd


# - Use the pd.concat() function to combine head_2015 and head_2016 along axis = 0 again. This time, however, set the
#   ignore_index parameter to True to reset the index in the result. Assign the result to concat_update_index.
#   - Use the variable inspector to view the results and confirm the index was reset.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    happiness2016 = pd.read_csv('World_Happiness_2016.csv')
    happiness2017 = pd.read_csv('World_Happiness_2017.csv')

    # Adding corresponding 'Year' column
    happiness2015['Year'] = 2015
    happiness2016['Year'] = 2016
    happiness2017['Year'] = 2017

    head_2015 = happiness2015[['Year', 'Country', 'Happiness Score', 'Standard Error']].head(4)
    head_2016 = happiness2016[['Country', 'Happiness Score', 'Year']].head(3)

    concat_update_index = pd.concat([head_2015, head_2016], ignore_index=True)


if __name__ == '__main__':
    main()
