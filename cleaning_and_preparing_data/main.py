def _open_data_set(file):
    """
    Open file and return a list of list (dataset).
    file it needs to be a csv file
    """
    from csv import reader
    with open(file) as opened_file:
        read_file = reader(opened_file)
        return list(read_file)


# Use a for loop to loop over the moma list of lists. In each iteration of the loop:
#
# Clean the Nationality column of the data set by:
# - Assigning the nationality for each row (found at list index 2 of the row) to a variable.
# - Using the str.replace() method to remove the open parentheses (() character.
# - Using the str.replace() method to remove the close parentheses ()) character.
# - Assigning the cleaned value back to list index 2 of the row.
# Clean the Gender column of the data set (found at index 5 of the row) by repeating the same technique you used for the Nationality column.
def main():
    moma = _open_data_set('artworks.csv')
    # Removing header row
    moma = moma[1:]

    for row in moma:
        # Cleaning the Nationality column, removing parenthesis => '(', ')'
        nationality = row[2]
        nationality = nationality.replace('(', '')
        nationality = nationality.replace(')', '')
        row[2] = nationality

        # Cleaning the Gender column, same of Nationality column
        gender = row[5]
        gender = gender.replace('(', '')
        gender = gender.replace(')', '')
        row[5] = gender

    for i in range(10):
        print('Title: ', moma[i][0], ' Nationality: ', moma[1][2], ' Gender: ', moma[1][5])


if __name__ == "__main__":
    main()
