import pandas as pd


# 1. Import the pandas library
# 2. Use the pandas.read_csv() function to read the laptops.csv file into a dataframe laptops.
# 3. Specify the encoding using the string "Latin-1".
#    Use the DataFrame.info() method to display information about the laptops dataframe.
def main():
    laptops = pd.read_csv('../laptops.csv', encoding='Latin-1')
    print(laptops.info())


if __name__ == '__main__':
    main()
