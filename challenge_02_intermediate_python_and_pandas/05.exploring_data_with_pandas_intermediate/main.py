import numpy as np
import pandas as pd


# 1. Create a new column roa in the f500 dataframe, containing the return on assets metric for each company.
# 2. Aggregate the data by the sector column, and create a dictionary top_roa_by_sector, with:
#     - Dictionary keys with the sector name.
#     - Dictionary values with the company name with the highest ROA value from that sector.
def main():
    f500 = pd.read_csv('../f500.csv')
    f500['roa'] = f500['profits'] / f500['assets']
    top_roa_by_sector = {}
    sectors = f500['sector'].unique()
    for s in sectors:
        top_roa_by_sector[s] = f500[f500['sector'] == s].sort_values('roa', ascending=False).iloc[0]['company']

    print(top_roa_by_sector)


if __name__ == "__main__":
    main()
