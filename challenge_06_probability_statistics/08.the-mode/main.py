import pandas as pd


# - Read in the TSV file (AmesHousing_1.txt) as a pandas DataFrame and save it to a variable named houses.
# - Explore the Land Slope column to find its scale of measurement. Refer to the documentation to find the data
#   dictionary of this column.
#   - Assign your answer as a string to the variable scale_land. Depending on the scale of measurement, choose between
#     these following strings: 'nominal', 'ordinal', 'interval', and 'ratio'.
# - Explore the Roof Style variable and find its scale of measurement. Assign your answer as a string to a variable
#   named scale_roof (choose between the four strings listed above).
#   - What measure of average would you choose for this column?
# - Explore the Kitchen AbvGr variable and determine whether it's continuous or discrete. Assign your answer as a string
#   to a variable named kitchen_variable — the string should be either 'continuous', or 'discrete'.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')
    print(houses['Land Slope'].value_counts())
    scale_land = 'ordinal'

    print(houses['Roof Style'].value_counts())
    scale_roof = 'nominal'

    print(houses['Kitchen AbvGr'].value_counts())
    kitchen_variable = 'discrete'


if __name__ == '__main__':
    main()
