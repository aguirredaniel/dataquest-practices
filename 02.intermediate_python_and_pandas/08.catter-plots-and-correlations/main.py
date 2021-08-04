import pandas as pd
import matplotlib.pyplot as plt


# - Generate a grouped frequency table for the registered column.
#   - The table must have 10 intervals.
#   - The intervals must be sorted in ascending order.
#   - Assign the table to the registered_freq variable.
# - Generate a grouped frequency table for the casual column.
#   - The table must have 10 intervals.
#   - The intervals must be sorted in an ascending order.
#   - Assign the table to the casual_freq variable.
def main():
    bike_sharing = pd.read_csv('../day.csv')
    bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

    registered_freq = bike_sharing['registered'].value_counts(bins=10).sort_index()
    casual_freq = bike_sharing['casual'].value_counts(bins=10).sort_index()

    print(registered_freq, casual_freq, sep='\n')


if __name__ == '__main__':
    main()
