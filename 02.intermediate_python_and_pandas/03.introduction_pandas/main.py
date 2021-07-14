import pandas as pd


# 1. Create a new variable big_movers, with:
#      - Rows with indices Aviva, HP, JD.com, and BHP Billiton, in that order.
#      - The rank and previous_rank columns, in that order.
# 2. Create a new variable, bottom_companies with:
#     - All rows with indices from National Grid to AutoNation, inclusive.
#     - The rank, sector, and country columns.

def main():
    f500 = pd.read_csv('../f500.csv', index_col=0)
    big_movers = f500.loc[['Aviva', 'HP', 'JD.com', 'BHP Billiton'], ['rank', 'previous_rank']]
    bottom_companies = f500.loc['National Grid': 'AutoNation', ['rank', 'sector', 'country']]

    print(big_movers, bottom_companies, sep='\n')


if __name__ == "__main__":
    main()
