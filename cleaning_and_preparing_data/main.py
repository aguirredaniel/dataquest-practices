def _open_data_set(file):
    """
    Open file and return a list of list (dataset).
    file it needs to be a csv file
    """
    from csv import reader
    with open(file) as opened_file:
        read_file = reader(opened_file)
        return list(read_file)


def _clean_and_convert(date: str):
    """
    Clean a year date value, removing parenthesis => '(', ')'.
    Return the date value as int.
    Example date param: '(1992)'
    """
    if not date:
        return date

    date = date.replace('(', '')
    date = date.replace(')', '')

    return int(date)


def strip_characters(string, bad_characters):
    """
    Iterates over a list of "bad" characters, and removing all occurrences in a string.
    """
    cleaned_string = string
    for bad_character in bad_characters:
        cleaned_string = cleaned_string.replace(bad_character, '')

    return cleaned_string


def process_date(string) -> int:
    """
    Process string value, if string is single date cast to int and return,
    if string contains a range of dates returns average of dates, cast to int and return,
    :param string: example of expected arguments '1992' or '1990-1994'
    :return int
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
