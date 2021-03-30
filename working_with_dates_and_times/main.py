import datetime as dt


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


# 1. Import the datetime class using the alias dt.
# 2. Instantiate a datetime object representing midnight on June 16, 1911.
#    Assign the object to the variable name ibm_founded.
# 3. Instantiate a datetime object representing 8:17 p.m. on July 20, 1969.
#    Assign the object to the variable name man_on_moon.
def main():
    ibm_founded = dt.datetime(1911, 6, 16)
    man_on_moon = dt.datetime(1969, 7, 20, 20, 17)

if __name__ == "__main__":
    main()
