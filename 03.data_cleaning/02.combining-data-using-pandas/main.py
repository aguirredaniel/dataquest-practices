import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# - Use either the pd.concat() function or the pd.merge() function to combine happiness2015, happiness2016, and
#   happiness2017. Assign the result to combined.
#   - Think about whether you need to combine the data horizontally or vertically in order to create a dataframe that
#     can be grouped by year, and decide which function (pd.concat() or pd.merge()) you can use to combine the data.
# - Use the df.pivot_table() method to create a pivot table from the combined dataframe. Set Year as the index and
#   Happiness Score as the values. Assign the result to pivot_table_combined.
# - Use the df.plot() method to create a bar chart of the results. Set the kind parameter to barh, the title to 'Mean
#   Happiness Scores by Year', and the xlim parameter to (0,10).
# - Try to answer the following question based on the results of this exercise: Did world happiness increase, decrease,
#   or stay about the same from 2015 to 2017?Use either the pd.concat() function or the pd.merge() function to combine
#   happiness2015, happiness2016, and happiness2017. Assign the result to combined.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    happiness2016 = pd.read_csv('World_Happiness_2016.csv')
    happiness2017 = pd.read_csv('World_Happiness_2017.csv')

    happiness2017.rename(columns={'Happiness.Score': 'Happiness Score'}, inplace=True)

    # Adding corresponding 'Year' column
    happiness2015['Year'] = 2015
    happiness2016['Year'] = 2016
    happiness2017['Year'] = 2017

    combined = pd.concat([happiness2015, happiness2016, happiness2017])
    pivot_table_combined = combined.pivot_table('Happiness Score', 'Year', aggfunc=np.mean)

    pivot_table_combined.plot(kind='barh', title='Mean Happiness Scores by Year', xlim=(0, 10))
    plt.show()


if __name__ == '__main__':
    main()
