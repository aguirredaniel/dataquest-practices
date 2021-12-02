import pandas as pd


# - The data set is stored in a file named AmesHousing_1.txt. Read the file as a pandas DataFrame, and store it in a
#   variable named houses.
#   - The values in each row are tab-separated, which means AmesHousing_1.txt is a TSV (tab-separated value) file. This
#     is different from a CSV (comma-separated values) file, where the values are separated by commas, not by a tab
#     character.
#    - Use the pd.read_table() function or pd.read_csv(sep = '\t') to read in the data set.
# - With the help of the documentation and by exploring the data set yourself, assess the truth value of the following
#   sentences:
#   - This data set has variables measured on every scale of measurement: nominal, ordinal, interval and ratio. (If you
#     think this is true, assign the boolean True to the variable one, otherwise assign False.)
#   - The SalePrice column is continuous and measured on an interval scale. (If you think this is true, assign the
#     boolean True to the variable two, otherwise assign False.)
#   - In the paper he published here, professor Dean DeCock wrote "The initial Excel file contained 113 variables
#     describing 3970 property sales that had occurred in Ames, Iowa between 2006 an 2010". If we wanted to measure the
#     mean sale prices for all the houses sold between 2006 and 2010 in Ames, Iowa, the data stored in the
#      AmesHousing_1.txt would be a sample. (If you think the last sentence is true, assign the boolean True to the
#      variable three, otherwise assign False.)
def main():
    houses = pd.read_csv('AmesHousing_1.txt', sep='\t')
    one = True
    two = False
    three = True

if __name__ == '__main__':
    main()
