import numpy as np
import pandas as pd


# 1. Select all companies with revenues over 100 billion and negative profits from the f500 dataframe. The result
#    should include all columns.
#    - Create a boolean array that selects the companies with revenues greater than 100 billion. Assign the result to
#      large_revenue.
#    - Create a boolean array that selects the companies with profits less than 0. Assign the result to
#      negative_profits.
#    - Combine large_revenue and negative_profits. Assign the result to combined.
#    - Use combined to filter f500. Assign the result to big_rev_neg_profit
def main():
    f500 = pd.read_csv('../f500.csv')
    large_revenue = f500['revenues'] > 100000
    negative_profits = f500['profits'] < 0
    combined = large_revenue & negative_profits
    big_rev_neg_profit = f500[combined]

    print(big_rev_neg_profit[['company', 'revenues', 'profits']])


if __name__ == "__main__":
    main()
