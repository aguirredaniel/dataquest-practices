import pandas as pd


# 1. Select the country column. Assign the result to the variable name countries.
# 2. In order, select the revenues and years_on_global_500_list columns. Assign the result to the variable name
#    revenues_years.
# 3. In order, select all columns from ceo up to and including sector. Assign the result to the variable name
#    ceo_to_sector.
def main():
    f500 = pd.read_csv('../f500.csv', index_col=1)
    countries = f500['country']
    revenues_years = f500[['revenues', 'years_on_global_500_list']]
    ceo_to_sector = f500.loc[:, 'ceo':'sector']
    print(countries, revenues_years, ceo_to_sector, sep='\n')


if __name__ == "__main__":
    main()
