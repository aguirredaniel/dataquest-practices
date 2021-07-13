import pandas as pd


# 1. Create a new variable toyota, with:
#     - Just the row with index Toyota Motor.
#     - All columns.
# 2. Create a new variable, drink_companies, with:
#     - Rows with indicies Anheuser-Busch InBev, Coca-Cola, and Heineken Holding, in that order.
#     - All columns.
# 3 . Create a new variable, middle_companies with:
#      - All rows with indicies from Tata Motors to Nationwide, inclusive.
#      - All columns from rank to country, inclusive.
def main():
    f500 = pd.read_csv('../f500.csv', index_col=0)
    toyota = f500.loc['Toyota Motor']
    drink_companies = f500.loc[['Anheuser-Busch InBev', 'Coca-Cola', 'Heineken Holding']]
    middle_companies = f500.loc['Tata Motors':'Nationwide', 'rank':'country']
    print(toyota, drink_companies, middle_companies, sep='\n')


if __name__ == "__main__":
    main()
