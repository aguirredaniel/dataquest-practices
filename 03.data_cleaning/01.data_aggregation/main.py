import pandas as pd


# * For the following exercise, use the result from the dictionary returned by grouped.groups shown below:
#   'North America': Int64Index([4, 14], dtype='int64'
# - Prove that the values for the "North America" group in the dictionary returned by grouped.groups above correspond to
#   countries in North America in the happiness2015 DataFrame.
#   - Use the snippet above to identify the indices of the countries in happiness2015 that belong to the North America
#     group.
#   - Use the indices to assign just the countries in North America in happiness2015 to north_america.
# - Use the GroupBy.get_group() method to select the data for the North America group only. Assign the result to
#   na_group.
# - Use the following code to compare north_america and na_group: north_america == na_group. Assign the result to equal.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    grouped = happiness2015.groupby('Region')
    means = grouped.mean()
    print(means)


if __name__ == '__main__':
    main()
