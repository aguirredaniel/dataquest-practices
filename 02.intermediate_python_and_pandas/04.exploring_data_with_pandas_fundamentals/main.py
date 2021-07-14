import pandas as pd


# 1. Subtract the values in the rank column from the values in the previous_rank column. Assign the result to
#    rank_change.
def main():
    f500 = pd.read_csv('../f500.csv')
    rank_change = f500['previous_rank'] - f500['rank']


if __name__ == "__main__":
    main()
