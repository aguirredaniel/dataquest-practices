import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# - Use the pd.merge() function to assign the REGION in the regions dataframe to the corresponding country in combined.
#   - Set the left parameter equal to combined.
#   - Set the right parameter equal to regions.
#   - Set the on parameter equal to 'COUNTRY'.
#   - Set the how parameter equal to 'left' to make sure we don't drop any rows from combined.
# - Assign the result back to combined.
#   - Use the DataFrame.drop() method to drop the original region column with missing values, now named REGION_x.
#   - Pass 'REGION_x' into the df.drop() method.
#   - Set the axis parameter equal to 1.
#   - Assign the result back to combined.
# - Use the DataFrame.isnull() and DataFrame.sum() methods to check for missing values. Assign the result to a variable
#   named missing.
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

    missing = combined.isnull().sum()

    print(missing)


if __name__ == '__main__':
    main()
