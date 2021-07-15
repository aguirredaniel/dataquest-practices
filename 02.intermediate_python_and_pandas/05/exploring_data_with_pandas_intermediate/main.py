import numpy as np
import pandas as pd


# 1. Select the rank, revenues, and revenue_change columns in f500. Then, use the DataFrame.head() method to select
#    the first five rows. Assign the result to f500_selection.
# 2. Use the variable inspector to view f500_selection. Compare the results to the first few lines of our CSV file
#    above.
def main():
    f500 = pd.read_csv('../f500.csv')
    f500.index.name = None

    f500.loc[f500['previous_rank'] == 0, 'previous_rank'] = np.nan

    f500_selection = f500[['rank', 'revenues', 'revenue_change']].head()

    print(f500_selection)


if __name__ == 'main':
    main()
