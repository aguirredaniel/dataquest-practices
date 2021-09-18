import pandas as pd


# - Use the pd.concat() function to combine head_2015 and head_2016 along axis = 0. Remember to pass the head_2015 and
#   head_2016 into the function as a list. Assign the result to concat_axis0.
# - Use the pd.concat() function to combine head_2015 and head_2016 along axis = 1. Remember to pass head_2015 and
#   head_2016 into the function as a list and set the axis parameter equal to 1. Assign the result to concat_axis1.
# - Use the variable inspector to view concat_axis0 and concat_axis1.
# - Assign the number of rows in concat_axis0 to a variable called question1.
# - Assign the number of rows in concat_axis1 to a variable called question2.
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

    concat_axis0 = pd.concat([head_2015, head_2016])
    concat_axis1 = pd.concat([head_2015, head_2016], axis=1)
    rows = 7
    columns = 4


if __name__ == '__main__':
    main()
