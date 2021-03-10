def _open_data_set(file):
    """  Open a csv file and return a list of list (dataset).

    Args:
        file: A string name of file to be open.

    Returns:
        A list of list that represent a dataset.
        For any row in file opened represent one dimension of list,
        the other dimension is represent for values in a row.

        For example:
        For file with this content
        a,b,c,d
        e,f,g,h
        i,j,k,l

        returns
        [['a','b','c','d']
         ['e','f','g','h']
         ['i','j','k','l']]
    """
    from csv import reader
    with open(file) as opened_file:
        read_file = reader(opened_file)
        return list(read_file)


def _clean_and_convert(date: str):
    """ Cleaning and convert a string that represent a year date value.

    Args:
        date: A string represent a year date value. Expected format for argument: '(1992)'

    Returns:
        A int as year date.
        For '(1992)' string argument  returns 1992 int value.
    """
    if not date:
        return date

    date = date.replace('(', '')
    date = date.replace(')', '')

    return int(date)


def strip_characters(string, bad_characters):
    """ Iterates over a list of "bad" characters, and removing all occurrences in a string.

    Args:
        string: A string for cleaning.
        bad_characters: A list of strings to removing occurrences in string param.

    Returns:
        A string with no bad characters.
    """
    cleaned_string = string
    for bad_character in bad_characters:
        cleaned_string = cleaned_string.replace(bad_character, '')

    return cleaned_string


def process_date(string) -> int:
    """Convert a string that represent a year date or time period to int value.

    Args:
        string: A string that represent a year date or time period.
        The format of string expected are: 'yyyy' or 'yyyy - yyyy'

    Returns:
        If string argument contains return int value of average of the time period.
        Else return int value of year date.

        For example:
        '1992-1995'
        returns
        1993

        for:
        '1992'
        returns
        1992
    """
    if '-' in string:
        split_string = string.split('-')
        start_date = int(split_string[0])
        end_date = int(split_string[1])
        average_date = (start_date + end_date) / 2
        return round(average_date)

    return int(string)


# 1. Create a function called strip_characters(), which accepts a string argument and:
#  - Iterates over the bad_chars list, using str.replace() to remove each character.
#  - Returns the cleaned string.
# 2. Create an empty list, stripped_test_data.
# 3. Iterate over the strings in test_data, and on each iteration:
# - Use the function you created earlier to clean the string.
# - Append the cleaned string to the stripped_test_data list.
def strip_characters_practice():
    test_data = ["1912", "1929", "1913-1923",
                 "(1951)", "1994", "1934",
                 "c. 1915", "1995", "c. 1912",
                 "(1988)", "2002", "1957-1959",
                 "c. 1955.", "c. 1970's",
                 "C. 1990-1999"]

    bad_chars = ["(", ")", "c", "C", ".", "s", "'", " "]

    stripped_test_data = [strip_characters(data, bad_chars) for data in test_data]

    print(stripped_test_data)


# 1. Create a function called process_date() which accepts a string, and follows the logic we outlined above:
#  - Checks if the dash character (-) is in the string so we know if it's a range or not.
#  - If it is a range:
#   - Splits the string into two strings, before and after the dash character.
#   - Converts the two numbers to the integer type and then average them by adding them together and dividing by two.
#   - Uses the round() function to round the average, so values like 1964.5 become 1964.
#  - If it isn't a range:
#  - Converts the value to an integer type.
#  - Finally, returns the value.
# 2. Create an empty list processed_test_data.
# 3. Loop over the stripped_test_data list using your process_date() function. Process the dates and append
#    each processed date back to the processed_test_data list.
def process_date_practice():
    stripped_test_data = ['1912', '1929', '1913-1923',
                          '1951', '1994', '1934',
                          '1915', '1995', '1912',
                          '1988', '2002', '1957-1959',
                          '1955', '1970', '1990-1999']

    processed_test_data = [process_date(data) for data in stripped_test_data]

    print(processed_test_data)


# 4. Once your code works with the test data, you can then iterate over the moma list of lists. In each iteration:
#  - Assign the value from the Date column (index 6) to a variable.
#  - Use the strip_characters() function to remove any bad characters.
#  - Use the process_date() to convert the date.
#  - Assign the stripped and processed value back to the row.
def main():
    moma = _open_data_set('artworks.csv')
    # Removing header row
    moma = moma[1:]

    for row in moma:
        # Cleaning the Nationality column, removing parenthesis => '(', ')'
        nationality = row[2]
        if nationality:
            nationality = nationality.replace('(', '')
            nationality = nationality.replace(')', '')
            # Capitalization uniform
            nationality = nationality.title()
        else:
            nationality = 'Nationality Unknown'

        row[2] = nationality

        # Cleaning the Gender column, same of Nationality column
        gender = row[5]
        if gender:
            gender = gender.replace('(', '')
            gender = gender.replace(')', '')
            # Exists 'Female', 'female', 'Male', 'male' values.
            # We'll use title built-in function to capitalization uniform.
            gender = gender.title()
        else:
            gender = 'Gender Unknown/Other'

        row[5] = gender

        # Cleaning BeginDate and EndDate columns
        begin_date = row[3]
        row[3] = _clean_and_convert(begin_date)

        end_date = row[4]
        row[4] = _clean_and_convert(end_date)

        # Cleaning Date column
        date_bad_chars = ["(", ")", "c", "C", ".", "s", "'", " "]
        date = row[6]
        date = strip_characters(date, date_bad_chars)
        row[6] = process_date(date)


if __name__ == "__main__":
    process_date_practice()
    main()
