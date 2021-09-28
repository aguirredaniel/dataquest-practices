import pandas as pd


# - Use the DataFrame.isnull() and DataFrame.sum() methods to confirm the number of missing values in happiness2016.
#   Assign the result to missing_2016.
# - Use the DataFrame.isnull() and DataFrame.sum() methods to confirm the number of missing values in happiness2017.
#   Assign the result to missing_2017.
def main():
    happiness2015 = pd.read_csv('wh_2015.csv')
    happiness2016 = pd.read_csv('wh_2016.csv')
    happiness2017 = pd.read_csv('wh_2017.csv')

    missing_2016 = happiness2016.isnull().sum()
    missing_2017 = happiness2017.isnull().sum()

    print(missing_2016, missing_2017, sep='\n')


if __name__ == '__main__':
    main()
