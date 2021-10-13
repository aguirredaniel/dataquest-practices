import numpy as np
import pandas as pd


# - Use Series.mask() to replace any null values from the total_injured column with their equivalents from the
#   injured_manual_sum series.
# - Use Series.mask() to replace any numbers from total_injured that aren't equal to their equivalents in
#   injured_manual_sum with np.nan.
def main():
    mvc = pd.read_csv('nypd_mvc_2018.csv')

    killed_cols = [col for col in mvc.columns if 'killed' in col]
    killed = mvc[killed_cols].copy()
    killed_manual_sum = killed.iloc[:, :3].sum(axis=1)

    killed_null_mask = killed['total_killed'].isnull()
    killed['total_killed'] = killed['total_killed'].mask(killed_null_mask, killed_manual_sum)

    killed_no_equal_mask = killed['total_killed'] != killed_manual_sum
    killed['total_killed'] = killed['total_killed'].mask(killed_no_equal_mask, np.nan)

    # Create an injured dataframe and manually sum values
    injured_columns = [col for col in mvc.columns if 'injured' in col]
    injured = mvc[injured_columns].copy()
    injured_manual_sum = injured.iloc[:, :3].sum(axis=1)

    injured_null_mask = injured['total_injured'].isnull()
    injured['total_injured'] = injured['total_injured'].mask(injured_null_mask, injured_manual_sum)

    injured_no_equal_mask = injured['total_injured'] != injured_manual_sum
    injured['total_injured'] = injured['total_injured'].mask(injured_no_equal_mask, np.nan)


if __name__ == '__main__':
    main()
