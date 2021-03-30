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
    END_DATE = 3


# 1. Instantiate an empty dictionary for our frequency table, appt_lengths.
# 2. Loop over each row in potus, and:
#  - Assign the values for appt_start_date (index 2) and appt_end_date (index 3) to variables.
#  - Subtract appt_start_date from appt_end_date to calculate the length of the appointment, length.
#  - If length is not a key in appt_lengths, add it as a key with a value of 1.
#  -    If length is a key in appt_lengths, add 1 to the existing value of that key.
# 3. Calculate the minimum key in appt_lengths and assign the result to min_length.
# 4. Calculate the maximum key in appt_lengths and assign the result to max_length.
def main():
    potus = _open_data_set('potus_visitors_2015.csv')
    # Removing row header
    potus = potus[1:]

    # strftime code for appt_start_date and end_date rows values
    date_format = '%m/%d/%y %H:%M'

    visitors_per_month = {}
    # strftime code to use as key for frequency table of visitors per month
    # example: 'October, 1992'
    month_format = '%B, %Y'

    appt_times = []

    appt_lengths = {}

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

        # Converting the end_date to datetime
        appt_end_date = row[POTUSRows.END_DATE]
        appt_end_date = row[POTUSRows.END_DATE] = dt.datetime.strptime(appt_end_date, "%m/%d/%y %H:%M")

        # Creating  visitors_per_month frequency table
        appt_length = appt_end_date - appt_start_date
        length_count = appt_lengths.get(appt_length, 0)
        appt_lengths[appt_length] = length_count + 1

    min_time = min(appt_times)
    max_time = max(appt_times)

    min_length = min(appt_lengths)
    max_length = max(appt_lengths)


if __name__ == "__main__":
    main()
