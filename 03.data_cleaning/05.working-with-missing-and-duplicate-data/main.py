import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# - Use the Series.mean() method to calculate the mean of the HAPPINESS SCORE column. Assign the result to
#   happiness_mean. Print happiness_mean.
# - Use the Series.fillna() method to replace all the missing values in the HAPPINESS SCORE column with happiness_mean.
#   Assign the result to a new column named HAPPINESS SCORE UPDATED.
# - Print the mean of HAPPINESS SCORE UPDATED.
# - Based on the results of this exercise, try to answer the question below:
#   - Did replacing missing values with the mean of a series cause the mean to change?
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

    combined.rename(columns={'REGION_y': 'REGION'}, inplace=True)

    combined['COUNTRY'] = combined['COUNTRY'].str.upper()
    combined = combined.drop_duplicates(['COUNTRY', 'YEAR'])

    columns_to_drop = ['LOWER CONFIDENCE INTERVAL', 'STANDARD ERROR', 'UPPER CONFIDENCE INTERVAL', 'WHISKER HIGH',
                       'WHISKER LOW']
    combined = combined.drop(columns_to_drop, axis=1)

    combined = combined.dropna(thresh=159, axis=1)

    # From the visualization above, we can also identify that only three regions contain missing values:
    #   Sub-Saharan Africa
    #   Middle East and Northern Africa
    #   Latin America and Carribbean
    # Only about 4 percent of the values in each column are missing.
    # Dropping rows with missing values won't cause us to lose information in other columns.
    sorted_values = combined.set_index('REGION').sort_values(['REGION', 'HAPPINESS SCORE'])
    sns.heatmap(sorted_values.isnull(), cbar=False)

    happiness_mean = combined['HAPPINESS SCORE'].mean()
    combined['HAPPINESS SCORE UPDATED'] = combined['HAPPINESS SCORE'].fillna(happiness_mean)
    print(happiness_mean, combined['HAPPINESS SCORE UPDATED'].mean(), sep='\n')


if __name__ == '__main__':
    main()
