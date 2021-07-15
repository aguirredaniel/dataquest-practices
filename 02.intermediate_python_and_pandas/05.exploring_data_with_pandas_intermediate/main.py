import numpy as np
import pandas as pd


# 1. Create an empty dictionary, top_employer_by_country to store the results of the exercise.
# 2. Use the Series.unique() method to create an array of unique values from the country column.
# 3. Use a for loop to iterate over the array unique countries. In each iteration:
#    - Select only the rows that have a country name equal to the current iteration.
#    - Use DataFrame.sort_values() to sort those rows by the employees column in descending order.
#    - Select the first row from the sorted dataframe.
#    - Extract the company name from the index label company from the first row.
#    - Assign the results to the top_employer_by_country dictionary, using the country name as the key, and the company
#      name as the value.
def main():
    f500 = pd.read_csv('../f500.csv')
    top_employer_by_country = {}
    countries = f500['country'].unique()
    for c in countries:
        top_employer_by_country[c] = f500[f500['country'] == c]. \
            sort_values('employees', ascending=False).iloc[0]['company']

    print(top_employer_by_country)


if __name__ == "__main__":
    main()
