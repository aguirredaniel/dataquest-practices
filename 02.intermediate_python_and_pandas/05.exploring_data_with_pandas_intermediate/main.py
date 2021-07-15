import numpy as np
import pandas as pd


# 1. Select all rows for companies whose country value is either Brazil or Venezuela. Assign the result to
#    brazil_venezuela.
# 2. Select the first five companies in the Technology sector for which the country is not the USA from the f500
#    dataframe. Assign the result to tech_outside_usa.
def main():
    f500 = pd.read_csv('../f500.csv')
    brazil_venezuela = f500[(f500['country'] == 'Brazil') | (f500['country'] == 'Venezuela')]
    tech_outside_usa = f500[(f500['sector'] == 'Technology') & (f500['country'] != 'USA')].head()

    print(brazil_venezuela['country'], tech_outside_usa[['sector', 'country']])


if __name__ == "__main__":
    main()
