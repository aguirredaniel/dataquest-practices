import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# - Confirm that the REGION column is missing from the 2017 data. Recall that there are 164 rows for the year 2017.
#   - Select just the rows in combined in which the YEAR column equals 2017. Then, select just the REGION column. Assign
#     the result to regions_2017.
#   - Use the Series.isnull() and Series.sum() to calculate the total number of missing values in regions_2017, the
#     REGION column for 2017. Assign the result to missing.
# - Use the variable inspector to view the results of missing. Are all 164 region values missing for the year 2017?
def main():
    happiness2015 = pd.read_csv('wh_2015.csv')
    happiness2016 = pd.read_csv('wh_2016.csv')
    happiness2017 = pd.read_csv('wh_2017.csv')

    happiness2015.columns = happiness2015.columns \
        .str.replace(r'[\(*\)]', '') \
        .str.replace(r'\s+', ' ') \
        .str.strip().str.upper()

    happiness2016.columns = happiness2016.columns \
        .str.replace(r'[\(*\)]', '') \
        .str.replace(r'\s+', ' ') \
        .str.strip().str.upper()
    happiness2017.columns = happiness2017.columns.str.replace('.', ' ').str.replace('\s+', ' ').str.strip().str.upper()

    combined = pd.concat([happiness2015, happiness2016, happiness2017], ignore_index=True)

    combined_updated = combined.set_index('YEAR')
    sns.heatmap(combined_updated.isnull(), cbar=False)
    plt.show()

    regions_2017 = combined[combined['YEAR'] == 2017]['REGION']
    missing = regions_2017.isnull().sum()


if __name__ == '__main__':
    main()
