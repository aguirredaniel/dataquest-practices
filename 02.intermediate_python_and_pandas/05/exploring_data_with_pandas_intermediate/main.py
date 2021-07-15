import numpy as np
import pandas as pd


# 1. Select just the fifth row of the f500 dataframe. Assign the result to fifth_row.
# 2. Select the value in first row of the company column. Assign the result to company_value.
def main():
    f500 = pd.read_csv('../f500.csv')
    fifth_row = f500.iloc[4]
    company_value = f500.iloc[0, 0]

    print(fifth_row, company_value, sep='\n')


if __name__ == 'main':
    main()
