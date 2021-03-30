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


# 1. Instantiate an empty appt_times list.
# 2. Iterate over each row in the potus list of lists. For each iteration:
#  - Assign the datetime object stored at index value 2 to a variable.
#  - Create a time object from the datetime object.
#  - Append the time object to the appt_times list.
def main():
    potus = _open_data_set('potus_visitors_2015.csv')
    # Removing row header
    potus = potus[1:]

    # strftime code for appt_start_date row values
    date_format = '%m/%d/%y %H:%M'

    visitors_per_month = {}
    # strftime code to use as key for frequency table of visitors per month
    # example: 'October, 1992'
    month_format = '%B, %Y'

    appt_times = []

    for row in potus:
        # Converting the appt_start_date to datetime
        appt_start_date = row[POTUSRows.APPT_START_DATE]
        appt_start_date = row[POTUSRows.APPT_START_DATE] = dt.datetime.strptime(appt_start_date, date_format)

        # Creating  visitors_per_month frequency table
        month = appt_start_date.strftime(month_format)
        visitors = visitors_per_month.get(month, 0)
        visitors_per_month[month] = visitors + 1

        # Getting time for appt_start_date
        appt_times.append(appt_start_date.time())


if __name__ == "__main__":
    main()
