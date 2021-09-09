import pandas as pd


# - Create an empty dictionary named mean_happiness to store the results of this exercise.
# - Use the Series.unique() method to create an array of unique values for the Region column.
# - Use a for loop to iterate over the unique region values from the Region column.
# - Assign the rows belonging to the current region to a variable named region_group.
# - Use the Series.mean() method to calculate the mean happiness score for region_group.
# - Assign the mean value to the mean_happiness dictionary, using the region name as the key and the mean happiness
#   score as the value.

def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')

    mean_happiness = {}
    regions = happiness2015['Region'].unique()
    for region in regions:
        region_group = happiness2015[happiness2015['Region'] == region]
        mean_happiness[region] = region_group['Happiness Score'].mean()
    print(mean_happiness)


if __name__ == '__main__':
    main()
