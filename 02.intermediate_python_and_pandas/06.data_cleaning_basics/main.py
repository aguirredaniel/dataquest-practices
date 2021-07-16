import pandas as pd


# 1. Remove any whitespace from the start and end of each column name.
#    - Create an empty list named new_columns.
#    - Use a for loop to iterate through each column name using the DataFrame.columns attribute. Inside the body of the
#      for loop:
#      - Use the str.strip() method to remove whitespace from the start and end of the string.
#      - Append the updated column name to the new_columns list.
#    - Assign the updated column names to the DataFrame.columns attribute.
def main():
    laptops = pd.read_csv('../laptops.csv', encoding='Latin-1')
    new_columns = []
    for c in laptops.columns:
        cleaned_column = c.strip()
        new_columns.append(cleaned_column)
    laptops.columns = new_columns

    print(laptops.info())

if __name__ == '__main__':
    main()
