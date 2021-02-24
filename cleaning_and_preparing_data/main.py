def _open_data_set(file):
    """
    Open file and return a list of list (dataset).
    file it needs to be a csv file
    """
    from csv import reader
    with open(file) as file_opened:
        file_reader = reader(file_opened)
        return list(file_reader)


# Write your answer to the instructions below -- the list of
# lists is stored using the variable name `moma`

def main():
    moma = _open_data_set('artworks.csv')
    num_rows = len(moma)
    print(num_rows)


if __name__ == "__main__":
    main()
