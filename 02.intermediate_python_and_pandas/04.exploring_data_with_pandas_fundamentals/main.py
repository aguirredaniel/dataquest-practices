import pandas as pd


# 1. Use Series.value_counts() and Series.loc to return the number of companies with a value of 0 in the previous_rank
#    column in the f500 dataframe. Assign the results to zero_previous_rank
def main():
    f500 = pd.read_csv('../f500.csv')
    zero_previous_rank = f500["previous_rank"].value_counts().loc[0]

    print(zero_previous_rank, sep='\n')


if __name__ == "__main__":
    main()
