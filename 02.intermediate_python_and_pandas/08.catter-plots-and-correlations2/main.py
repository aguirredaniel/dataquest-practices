import pandas as pd


# - Import the pandas module as pd.
# - Read in the day.csv file using the pd.read_csv() function. Assign the result to a variable named bike_sharing.
# - Examine the first and the last five rows.
# - Display information about the dataset using the DataFrame.info() method. How many rows and columns does this dataset
#   have? Do you see any missing values?
def main():
    bike_sharing = pd.read_csv('../day.csv')
    print(bike_sharing.head())
    print(bike_sharing.tail())
    print(bike_sharing.info(()))


if __name__ == '__main__':
    main()
