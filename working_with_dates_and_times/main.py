import datetime as dt

from enum import IntEnum


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


class POTUSRows(IntEnum):
    """ An Enum that helps make the code expressive when the POTUS dataset columns are mapped.
      """
    APPT_START_DATE = 2


# 1. Create a string date_format that specifies the format of the appt_start_date column:
#  - The format of the app_start_date column is {month}/{day}/{two digit year} {hour 24hr time}:{minute}.
#  - Substitute each of the values inside braces with the appropriate strftime code from the table above.
# 2. Iterate over each row in the potus list of lists:
#  - Assign the appt_start_date column, found at index 2 of each row, to a variable.
#  - Use the datetime.strptime() constructor to convert the variable from a string to a datetime object,
#    using the date_format string you created earlier.
#  - Assign the datetime object back to index 2 of the row.
def main():
    potus = _open_data_set('potus_visitors_2015.csv')
    # Removing row header
    potus = potus[1:]

    # strftime code for appt_start_date row values
    date_format = '%m/%d/%y %H:%M'

    for row in potus:
        appt_start_date = row[POTUSRows.APPT_START_DATE]
        row[POTUSRows.APPT_START_DATE] = dt.datetime.strptime(appt_start_date, date_format)


if __name__ == "__main__":
    main()
