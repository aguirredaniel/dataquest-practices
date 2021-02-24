def _open_data_set(file):
    """
    Open file and return a list of list (dataset).
    file it needs to be a csv file
    """
    from csv import reader
    with open(file) as opened_file:
        read_file = reader(opened_file)
        return list(read_file)


# Use the open() function to open the artworks.csv file. Assign the result to opened_file.
# Use the reader() function to parse the data from opened_file. Assign the result to read_file.
# Use list() to convert read_file into a list of lists. Assign the result to moma.
# Use list slicing to remove the column names (the first row) from the moma list of lists.
def main():
    moma = _open_data_set('artworks.csv')
    moma = moma[1:]
    print(moma[:10])


if __name__ == "__main__":
    main()
