import numpy as np
import pandas as pd


# 1. Create a series, industry_usa, containing counts of the two most common values in the industry column for companies
#    headquartered in the USA.
# 2. Create a series, sector_china, containing counts of the three most common values in the sector column for companies
#    headquartered in the China.
def main():
    f500 = pd.read_csv('../f500.csv')
    industry_usa = f500.loc[f500['country'] == 'USA', 'industry'].value_counts().head(2)
    sector_china = f500.loc[f500['country'] == 'China', 'sector'].value_counts().head(3)
    print(industry_usa, sector_china)


if __name__ == "__main__":
    main()
