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


# - Uncomment the commented lines (you might want to use this keyboard shortcut).
# - Add code to the body of the loop that:
#   - Creates a boolean mask for values where the vehicle column is null and the cause column is non-null.
#   - Creates a boolean mask for values where the cause column is null and the vehicle column is non-null.
#   - Uses the first boolean mask to fill matching values from the vehicle column with the string Unspecified.
#   - Uses the second boolean mask to fill matching values from the cause column with the string Unspecified.
#  - Outside the loop, use the summarize_missing() function to check that you have removed all matching values. Assign
#    the result to summary_after.
def main():
    mvc = pd.read_csv('nypd_mvc_2018.csv')

    impute_total_of_group_columns(mvc)

    summary_before = summarize_missing(mvc)

    for v in range(1, 6):
        v_col = 'vehicle_{}'.format(v)
        c_col = 'cause_vehicle_{}'.format(v)

        v_missing_mask = mvc[v_col].isnull() & mvc[c_col].notnull()
        c_missing_mask = mvc[v_col].notnull() & mvc[c_col].isnull()

        mvc[v_col] = mvc[v_col].mask(v_missing_mask, 'Unspecified')
        mvc[c_col] = mvc[c_col].mask(c_missing_mask, 'Unspecified')

    summary_after = summarize_missing(mvc)

    print(summary_before, summary_after, sep='\n\n')


if __name__ == '__main__':
    main()
