import numpy as np
import pandas as pd


# 1. Find the company headquartered in Japan with the largest number of employees.
#    - Select only the rows that have a country name equal to Japan.
#    - Use DataFrame.sort_values() to sort those rows by the employees column in descending order.
#    - Use DataFrame.iloc[] to select the first row from the sorted dataframe.
#    - Extract the company name from the index label company from the first row. Assign the result to
#      top_japanese_employer.
def main():
    f500 = pd.read_csv('../f500.csv')
    top_japanese_employer = f500[(f500['country'] == 'Japan')].sort_values('employees', ascending=False)['company'].iloc[0]
    print(top_japanese_employer)


if __name__ == "__main__":
    main()
