import pandas as pd


# - Create a series that counts the number of null values in each of the columns in the mvc dataframe. Assign the result
#   to null_counts.
def main():
    mvc = pd.read_csv('nypd_mvc_2018.csv')
    null_counts = mvc.isnull().sum()

    print(null_counts)


if __name__ == '__main__':
    main()
