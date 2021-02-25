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


# Use a for loop to iterate over each row in the moma list of lists. In each iteration:
# Assign the BeginDate and EndDate values (at indexes 3 and 4) to variables.
# Use the clean_and_convert() function to clean and convert each value.
# Assign the converted values back to indexes 3 and 4 so the cleaned values are used in the moma list of lists.
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


if __name__ == "__main__":
    strip_characters_practice()
