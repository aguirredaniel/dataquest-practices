import numpy as np
import pandas as pd


# 1. Select the first three rows of the f500 dataframe. Assign the result to first_three_rows.
# 2. Select the first and seventh rows and the first five columns of the f500 dataframe. Assign the result to
#    first_seventh_row_slice.
def main():
    f500 = pd.read_csv('../f500.csv')
    first_three_rows = f500.iloc[:3]
    first_seventh_row_slice = f500.iloc[[0, 6], :5]

    print(first_three_rows, first_seventh_row_slice, sep='\n')


if __name__ == 'main':
    main()
