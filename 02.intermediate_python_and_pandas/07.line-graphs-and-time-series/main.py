import matplotlib.pyplot as plt
import pandas as pd


# - Import the pandas module as pd.
# - Read in the WHO_time_series.csv file using the pd.read_csv() function. Assign the resulting DataFrame to a
#   variable named who_time_series.
# - Transform the Date_reported column to a datetime data type using pd.to_datetime(). Assign the DataFrame with the
#   modified column back to the who_time_series variable.
# - Print the first and the last five rows and examine the data points. Be sure to specify print().
# - Print information about the dataset using the DataFrame.info() method. How many rows and columns does the dataset
#   have? Do you see any missing values?
def main():
    who_time_series = pd.read_csv('WHO_time_series.csv')
    who_time_series['Date_reported'] = pd.to_datetime(who_time_series['Date_reported'], format='%Y-%m-%d')

    print(who_time_series.head())
    print(who_time_series.tail())
    print(who_time_series.info())


if __name__ == '__main__':
    main()
