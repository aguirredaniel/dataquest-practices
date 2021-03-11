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


def artist_summary(artis_name, freq_table):
    """ Print summary about of artist artworks.

    The format is next:
    There are {artworks} by {artis_name} in the data set

    Args:
        artis_name: An string with name of artist
        freq_table: An dict represent frequency table of artworks by the artist
    Returns:
        None
    """

    template = "There are {artworks} artworks by {artis_name} in the data set"
    artworks = freq_table.get(artis_name, 0)

    result = template.format(artis_name=artis_name, artworks=artworks)
    print(result)


class MoMAColumns(IntEnum):
    """ An Enum that helps make the code expressive when the MoMa dataset columns are mapped.
    """
    ARTIST_NAME = 1
    BIRTH_DATE = 3
    DATE = 6


# 1. Create a function artist_summary() which accepts a single argument, the name of an artist.
# 2. The function should print a summary of the artist using the steps below:
#  - Retrieve the number of artworks from the artist_freq dictionary, and assign it to a variable.
#  - Create a template string that uses braces ({}) to insert the name and variables into the string,
#    using the format from the diagram above.
#  - Use str.format() method to insert the artist's name and number of artworks into the string template.
#  - Use the print() function to display the final string.
# 3. Use your function to display a summary for the Artist "Henri Matisse".
def main():
    moma = _open_data_set('artworks_clean.csv')
    # Removing the row header
    moma = moma[1:]

    # Creating artist artwork frequency table
    artist_freq = {}
    for row in moma:
        artist_name = row[MoMAColumns.ARTIST_NAME]

        freq = artist_freq.get(artist_name, 0)
        artist_freq[artist_name] = freq + 1

    artist_summary('Henri Matisse', artist_freq)


if __name__ == "__main__":
    main()
