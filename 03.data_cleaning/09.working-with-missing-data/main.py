import pandas as pd


# - Select the first three columns from killed and sum each row. Assign the result to killed_manual_sum.
# - Create a boolean mask that checks whether each value in killed_manual_sum is not equal to the values in
#   the total_killed column. Assign the boolean mask to killed_mask.
# - Use killed_mask to filter the rows in killed. Assign the result to killed_non_eq.
def main():
    mvc = pd.read_csv('nypd_mvc_2018.csv')

    killed_cols = [col for col in mvc.columns if 'killed' in col]
    killed = mvc[killed_cols].copy()
    killed_manual_sum = killed.iloc[:, :3].sum(axis=1)
    killed_mask = killed['total_killed'] != killed_manual_sum
    killed_non_eq = killed[killed_mask]
    print(killed_non_eq)


if __name__ == '__main__':
    main()
