import numpy as np
import pandas as pd


# 1. Add a new column named rank_change to the f500 dataframe by subtracting the values in the rank column from the
#    values in the previous_rank column.
# 2. Use the Series.describe() method to return a series of descriptive statistics for the rank_change column. Assign
#    the result to rank_change_desc
def main():
    f500 = pd.read_csv('../f500.csv')
    f500['rank_change'] = f500['rank'] - f500['previous_rank']
    rank_change_desc = f500['rank_change'].describe()

    print(rank_change_desc)


if __name__ == "__main__":
    main()
