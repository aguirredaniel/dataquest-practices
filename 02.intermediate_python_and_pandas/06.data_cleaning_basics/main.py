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


# 1. Extract the manufacturer name from the cpu column. Assign it to a new column cpu_manufacturer.
# 2. Use the Series.value_counts() method to find the counts of each manufacturer in cpu_manufacturer. Assign the result
#    to cpu_manufacturer_counts.
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

    # extract the manufacturer name from the cpu column and assign it to a new column.
    laptops['cpu_manufacturer'] = laptops['cpu'].str.split().str[0]

    # correct the values in the os column.
    mapping_dict = {
        'Android': 'Android',
        'Chrome OS': 'Chrome OS',
        'Linux': 'Linux',
        'Mac OS': 'macOS',
        'No OS': 'No OS',
        'Windows': 'Windows',
        'macOS': 'macOS'
    }

    laptops['os'] = laptops['os'].map(mapping_dict)


if __name__ == '__main__':
    main()
