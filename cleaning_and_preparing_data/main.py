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


def _clean_and_convert(date: str):
    """ Cleaning and convert a string that represent a year date value.

    Args:
        date: A string represent a year date value. Expected format for argument: '(1992)'

    Returns:
        A int as year date.
        For '(1992)' string argument  returns 1992 int value.
    """
    if not date:
        return date

    date = date.replace('(', '')
    date = date.replace(')', '')

    return int(date)


def strip_characters(string, bad_characters):
    """ Iterates over a list of "bad" characters, and removing all occurrences in a string.

    Args:
        string: A string for cleaning.
        bad_characters: A list of strings to removing occurrences in string param.

    Returns:
        A string with no bad characters.
    """
    cleaned_string = string
    for bad_character in bad_characters:
        cleaned_string = cleaned_string.replace(bad_character, '')

    return cleaned_string


def process_date(string) -> int:
    """Convert a string that represent a year date or time period to int value.

    Args:
        string: A string that represent a year date or time period.
        The format of string expected are: 'yyyy' or 'yyyy - yyyy'

    Returns:
        If string argument contains return int value of average of the time period.
        Else return int value of year date.

        For example:
        '1992-1995'
        returns
        1993

        for:
        '1992'
        returns
        1992
    """
    if '-' in string:
        split_string = string.split('-')
        start_date = int(split_string[0])
        end_date = int(split_string[1])
        average_date = (start_date + end_date) / 2
        return round(average_date)

    return int(string)


class MoMAColumns(IntEnum):
    """ An Enum that helps make the code expressive when the MoMa dataset columns are mapped.
    """
    BIRTH_DATE = 3
    DATE = 6


def main():
    moma = _open_data_set('artworks_clean.csv')
    # Removing the row header
    moma = moma[1:]

    ages = []
    for row in moma:
        birth_date = row[MoMAColumns.BIRTH_DATE]
        # Converting date row values to integer type
        date = row[MoMAColumns.DATE]
        if date:
            date = row[6] = int(date)

        # Calculating the age of artist when they made their artwork
        # If birth_date has no value, then age is assign to 0
        age = date - int(birth_date) if birth_date else 0
        ages.append(age)

    final_ages = []
    for age in ages:
        final_age = age if age > 20 else 'Unknown'
        final_ages.append(final_age)

    # Calculating the decade in which the artist created each work.
    decades = []
    for age in final_ages:
        if age == 'Unknown':
            decade = age
        else:
            # Removing the las digit of age we can calculate the decade,
            # it would be necessary to add 0s to comply with the format specified in practice
            decade = str(age)
            decade = decade[:-1]
            decade += '0s'
        decades.append(decade)

    # Calculating decade frequency table.
    decade_frequency = {}
    for decade in decades:
        decade_freq = decade_frequency.get(decade, 0)
        decade_frequency[decade] = decade_freq + 1


# 1. Create a template string to insert the artist and birth_year variables into a
#    string, using the format provided above. You may use your choice of the three
#    techniques you learned for specifying which variables goes where.
# 2. Use str.format() to insert the two variables into your template string, assigning the result to a variable.
# 3. Use the print() function to call that variable.

def string_format_practice():
    artist = "Pablo Picasso"
    birth_year = 1881

    template = "{}'s birth year is {}"
    result = template.format(artist, birth_year)

    print(result)


if __name__ == "__main__":
    string_format_practice()
