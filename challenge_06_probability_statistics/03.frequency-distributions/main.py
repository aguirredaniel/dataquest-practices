import pandas as pd


# - Using the techniques above, generate a grouped frequency table for the PTS variable. The table should have the
#   following characteristics:
# - There are 10 class intervals.
# - The first class interval starts at 0 (not included).
# - The last class interval ends at 600 (included).
# - Each interval has a range of 60 points.
# - Assign the table to a variable named gr_freq_table_10.
def main():
    pd.options.display.max_rows = 200
    pd.options.display.max_columns = 50

    wnba = pd.read_csv('../data/wnba.csv')

    intervals = pd.interval_range(start=0, end=600, freq=60)
    gr_freq_table_10 = pd.Series([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], index=intervals)

    for value in wnba['PTS']:
        for interval in intervals:
            if value in interval:
                gr_freq_table_10.loc[interval] += 1
                break
    print(gr_freq_table_10)


if __name__ == '__main__':
    main()
