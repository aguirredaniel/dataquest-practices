import pandas as pd


# 1. Define a function, which accepts a string argument, and:
#    - Removes any whitespace from the start and end of the string.
#    - Replaces the substring Operating System with the abbreviation os.
#    - Replaces all spaces with underscores.
#    - Removes parentheses from the string.
#    - Makes the entire string lowercase.
#    - Returns the modified string.
# 2. Use a loop to apply the function to each item in the DataFrame.columns attribute for the laptops dataframe. Assign
#    the result back to the DataFrame.columns attribute.

def clean_column_name(column):
    """
    Return a clean name for a column.
    The process make:
        - Removes any whitespace from the start and end of the string.
        - Replaces the substring Operating System with the abbreviation os.
        - Replaces all spaces with underscores.
        - Removes parentheses from the string.
        - Makes the entire string lowercase.
        - Returns the modified string.

    Parameters
    ----------
    column : string
        An column name.

    Raises
    ------
    ValueError
        If column parm is None or not a str.

    Examples
    --------
    Consider a column name
    >>> column_name = 'Model Name'
    >>> clean_column_name(column_name)
    'model_name'

    >>> column_name = 'Operating System Version'
    >>> column_name = clean_column_name(column_name)
    'os_version'

    >>> column_name = ' Price (Euros) '
    >>> column_name = clean_column_name(column_name)
    'price_euros'
    """
    if column is None or not isinstance(column, str):
        raise ValueError('The column is None or not a string.🙁')

    clean_column = column.strip()
    clean_column = clean_column.replace('Operating System', 'os')
    clean_column = clean_column.replace(' ', '_')
    clean_column = clean_column.replace('(', '').replace(')', '')
    clean_column = clean_column.lower()

    return clean_column


def main():
    laptops = pd.read_csv('../laptops.csv', encoding='Latin-1')
    new_columns = []
    for c in laptops.columns:
        clean_column = clean_column_name(c)
        new_columns.append(clean_column)
    laptops.columns = new_columns

    print(laptops.info())


if __name__ == '__main__':
    main()
