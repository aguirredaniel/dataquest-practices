import numpy as np
import pandas as pd


# 1. Assign the first five rows of the null_previous_rank dataframe to the variable top5_null_prev_rank by choosing
#    the correct method out of either loc[] or iloc[].
def main():
    f500 = pd.read_csv('../f500.csv')
    null_previous_rank = f500[f500["previous_rank"].isnull()]
    top5_null_prev_rank = null_previous_rank.iloc[:5]

    print(top5_null_prev_rank)


if __name__ == "__main__":
    main()
