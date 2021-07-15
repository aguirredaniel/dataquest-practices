import numpy as np
import pandas as pd


# 1. Use the Series.notnull() method to select all rows from f500 that have a non-null value for the previous_rank
#    column. Assign the result to previously_ranked
# 2. From the previously_ranked dataframe, subtract the rank column from the previous_rank column. Assign the result
#    to rank_change.
# 3. Assign the values in the rank_change to a new column in the f500 dataframe, "rank_change".
def main():
    f500 = pd.read_csv('../f500.csv')
    previously_ranked = f500[f500["previous_rank"].notnull()]
    rank_change = previously_ranked['previous_rank'] - previously_ranked['rank']
    f500['rank_change'] = rank_change

    print(f500[['company', 'previous_rank', 'rank', 'rank_change']])


if __name__ == "__main__":
    main()
