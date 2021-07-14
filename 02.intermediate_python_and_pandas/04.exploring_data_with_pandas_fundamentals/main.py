import numpy as np
import pandas as pd


# 1. Use boolean indexing to update values in the previous_rank column of the f500 dataframe:
#     - There should now be a value of np.nan where there previously was a value of 0.
#     - It is up to you whether you assign the boolean series to its own variable first, or whether you complete the
#       operation in one line.
# 2. Create a new pandas series, prev_rank_after, using the same syntax that was used to create the prev_rank_before
#    series.
def main():
    f500 = pd.read_csv('../f500.csv')
    f500.loc[f500['previous_rank'] == 0, 'previous_rank'] = np.nan
    prev_rank_after = f500['previous_rank'].value_counts(dropna=False).head()

    print(prev_rank_after)


if __name__ == "__main__":
    main()
