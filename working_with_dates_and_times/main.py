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


# 1. Use the open() function to open the CSV file potus_visitors_2015.csv
# 2. Use the reader() function to read the opened file.
# 3. Use the list() function to convert the read file into a list of lists format.
#  - Assign the list of lists to the variable name potus.
#  - Remove the first row of the data set, which contains the column names
def main():
    potus = _open_data_set('potus_visitors_2015.csv')
    potus = potus[1:]


if __name__ == "__main__":
    main()
