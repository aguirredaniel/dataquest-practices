import numpy as np
import pandas as pd
import re


def first_10_matches(titles: pd.Series, pattern: str):
    """
    Return the first 10 story titles that match
    the provided regular expression
    """
    all_matches = titles[titles.str.contains(pattern)]
    first_10 = all_matches.head(10)
    return first_10


# - Write a regular expression pattern which will match Python or python, followed by a space, followed by one or more
#   digit characters or periods.
#   - The regular expression should contain a capture group for the digit and period characters (the Python versions)
# - Extract the Python versions from titles using the regular expression pattern.
# - Use Series.value_counts() and the dict() function to create a dictionary frequency table of the extracted Python
#   versions. Assign the result to py_versions_freq.
def main():
    hn = pd.read_csv('hacker_news.csv')
    titles = hn["title"]

    pattern = r"[Pp]ython ([\d\.]+)"
    py_versions = titles.str.extract(pattern, expand=False)
    py_versions_freq = dict(py_versions.value_counts())
    print(py_versions_freq)


if __name__ == '__main__':
    main()
