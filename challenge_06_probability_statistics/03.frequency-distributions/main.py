import pandas as pd


# - Examine the frequency table for the PTS (total points) variable trying to find some patterns in the distribution of
#   values. Then, generate a grouped frequency distribution table for the PTS variable with the following
#   characteristics:
# - The table has 10 class intervals.
# - For each class interval, the table shows percentages instead of frequencies.
# - The class intervals are sorted in descending order.
# - Assign the table to a variable named grouped_freq_table, then print it and try again to find some patterns in the
#  distribution of values.
def main():
    pd.options.display.max_rows = 200
    pd.options.display.max_columns = 50

    wnba = pd.read_csv('../data/wnba.csv')

    grouped_freq_table = (wnba['PTS'].value_counts(bins=10, normalize=True) * 100).sort_index(ascending=False)
    print(grouped_freq_table)


if __name__ == '__main__':
    main()
