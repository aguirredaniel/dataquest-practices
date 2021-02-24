def _open_data_set(file):
    """
    Open file and return a list of list (dataset).
    file it needs to be a csv file
    """
    from csv import reader
    with open(file) as opened_file:
        read_file = reader(opened_file)
        return list(read_file)


# 1. Clean the Gender column.
# - Assign the value from the Gender column, at index 5, to a variable.
# - Make the changes to the value of that variable.
# - Use the str.title() method to make the capitalization uniform.
# - Use an if statement to check if the value is an empty string. If the value is an empty string, give it the value "Gender Unknown/Other".
# - Assign the modified variable back to list index 5 of the row.
# 2. Clean the Nationality column of the data set (found at index 2) by repeating the same technique you used for the Gender column.
# - For missing values in the Nationality column, use the string "Nationality Unknown".
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


if __name__ == "__main__":
    main()
