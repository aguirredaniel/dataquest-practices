import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# - Standardize the capitalization so that all the values in the COUNTRY column in combined are uppercase.
#   - As an example, 'India' should be changed to 'INDIA'.
# - Use the df.duplicated() method to identify any rows that have the same value in the COUNTRY and YEAR columns. Assign
#   your result to dups.
# - Use dups to index combined. Print the results.
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

    regions = pd.merge(happiness2015, happiness2016, on='COUNTRY')
    regions['REGION'] = regions.apply(
        lambda row: row['REGION_y'] if not pd.isna(row['REGION_y']) else row['REGION_x'],
        axis=1)
    regions = regions[['COUNTRY', 'REGION']]

    combined = pd.merge(combined, regions, on='COUNTRY', how='left')
    combined = combined.drop('REGION_x', axis=1)

    combined.rename({'REGION_x': 'REGION'}, inplace=True)

    combined['COUNTRY'] = combined['COUNTRY'].str.upper()
    dups = combined.duplicated(['COUNTRY', 'YEAR'])

    print(combined[dups])


if __name__ == '__main__':
    main()
