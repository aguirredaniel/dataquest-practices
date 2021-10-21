import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plot_null_correlations(df):
    # create a correlation matrix only for columns with at least
    # one missing value
    cols_with_missing_values = df.columns[df.isnull().sum() > 0]
    missing_corr = df[cols_with_missing_values].isnull().corr()

    # create a mask to avoid repeated values and make
    # the plot easier to read
    missing_corr = missing_corr.iloc[1:, :-1]
    # see triu: https://numpy.org/doc/stable/reference/generated/numpy.triu.html
    # >>> np.triu([[1,2,3],[4,5,6],[7,8,9],[10,11,12]], -1)
    # array([[ 1,  2,  3],
    #        [ 4,  5,  6],
    #        [ 0,  8,  9],
    #        [ 0,  0, 12]])
    # see ones_like: https://numpy.org/doc/stable/reference/generated/numpy.ones_like.html
    # >>> x = np.arange(6)
    # >>> x = x.reshape((2, 3))
    # >>> x
    # array([[0, 1, 2],
    #        [3, 4, 5]])
    # >>>> np.ones_like(x)
    # array([[1, 1, 1],
    #        [1, 1, 1]])
    mask = np.triu(np.ones_like(missing_corr), k=1)

    # plot a heatmap of the values
    plt.figure(figsize=(20, 14))
    ax = sns.heatmap(missing_corr, vmin=-1, vmax=1, cbar=False,
                     cmap='RdBu', mask=mask, annot=True)

    # format the text in the plot to make it easier to read
    for text in ax.texts:
        t = float(text.get_text())
        if -0.05 < t < 0.01:
            text.set_text('')
        else:
            text.set_text(round(t, 2))
        text.set_fontsize('x-large')
    plt.xticks(rotation=90, size='x-large')
    plt.yticks(rotation=0, size='x-large')

    plt.show()


def impute_total_of_group_columns(mvc: pd.DataFrame):
    """
        Impute the missing data in columns 'total_killed' and 'total_injured'
    Args:
        mvc:
         The nypd_mvc_2018.csv pd.DataFrame
    Returns:
        None
    """
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

    mvc['total_killed'] = killed['total_killed']
    mvc['total_injured'] = injured['total_injured']


def summarize_missing(mvc: pd.DataFrame) -> pd.DataFrame:
    """
         Count missing values across the pairs of columns of vehicle_n and cause_vehicle_n.
    Args:
        mvc:
         The nypd_mvc_2018.csv pd.DataFrame
    Returns:
        pd.DataFrame with columns ["vehicle_number", "vehicle_missing", "cause_missing"].
    """
    v_missing_data = []

    for v in range(1, 6):
        v_col = 'vehicle_{}'.format(v)
        c_col = 'cause_vehicle_{}'.format(v)

        v_missing = (mvc[v_col].isnull() & mvc[c_col].notnull()).sum()
        c_missing = (mvc[c_col].isnull() & mvc[v_col].notnull()).sum()

        v_missing_data.append([v, v_missing, c_missing])

    col_labels = columns = ["vehicle_number", "vehicle_missing", "cause_missing"]
    return pd.DataFrame(v_missing_data, columns=col_labels)


def impute_vehicle_and_cause(mvc: pd.DataFrame):
    """
    - For vehicle_n column is null and the cause_n column is non-null, fill vehicle column with the string 'Unspecified'
    - For vehicle_n column is non-null and the cause_n column is null, fill cause column with the string 'Unspecified'
    Args:
        mvc:
         The nypd_mvc_2018.csv pd.DataFrame
    Returns:
        None
    """

    for v in range(1, 6):
        v_col = 'vehicle_{}'.format(v)
        c_col = 'cause_vehicle_{}'.format(v)

        v_missing_mask = mvc[v_col].isnull() & mvc[c_col].notnull()
        c_missing_mask = mvc[v_col].notnull() & mvc[c_col].isnull()

        mvc[v_col] = mvc[v_col].mask(v_missing_mask, 'Unspecified')
        mvc[c_col] = mvc[c_col].mask(c_missing_mask, 'Unspecified')


# - Loop over the column names in location_cols. In each iteration of the loop, use Series.mask() to replace values in
#   the column in the mvc dataframe:
#   - The mask should represent whether the values in column in the mvc has a null value or not.
#   - Where the mask is true, the value should be replaced with the equivalent value in sup_data.
# - Calculate the number of null values across the location_cols columns in mvc after you adding the supplemental data.
#   Assign the result to null_after.
def main():
    mvc = pd.read_csv('nypd_mvc_2018.csv')
    sup_data = pd.read_csv('supplemental_data.csv')

    impute_total_of_group_columns(mvc)
    impute_vehicle_and_cause(mvc)

    location_cols = ['location', 'on_street', 'off_street', 'borough']
    null_before = mvc[location_cols].isnull().sum()

    for col in location_cols:
        missing_mask = mvc[col].isnull()
        mvc[col] = mvc[col].mask(missing_mask, sup_data[col])

    null_after = mvc[location_cols].isnull().sum()

    print(null_before, null_after, sep='\n\n')


if __name__ == '__main__':
    main()
