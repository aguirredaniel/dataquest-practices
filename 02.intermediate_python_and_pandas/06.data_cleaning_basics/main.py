import pandas as pd


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


# 1. Because the GB characters contained useful information about the units (gigabytes) of the laptop's ram, use the
#    DataFrame.rename() method to rename the column from ram to ram_gb.
# 2. Use the Series.describe() method to return a series of descriptive statistics for the ram_gb column. Assign the
#    result to ram_gb_desc.
def main():
    laptops = pd.read_csv('../laptops.csv', encoding='Latin-1')

    # re-asign columns name
    new_columns = []
    for c in laptops.columns:
        clean_column = clean_column_name(c)
        new_columns.append(clean_column)
    laptops.columns = new_columns

    # substring GB from the ram colum
    laptops['ram'] = laptops['ram'].str.replace('GB', '')

    # change the ram column to an integer dtype
    laptops['ram'] = laptops['ram'].astype(int)

    # rename the column from ram to ram_gb
    laptops.rename({'ram': 'ram_gb'}, axis=1, inplace=True)
    ram_gb_desc = laptops['ram_gb'].describe()

    print(ram_gb_desc)


if __name__ == '__main__':
    main()
