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


# - Uncomment the line of code. Add a negative set to the end of the regular expression that excludes:
#   - The period character .
#   - The plus character +.
# - Use the first_10_matches() function to return the matches for the regular expression you built, assigning the result to first_ten.
def main():
    hn = pd.read_csv('hacker_news.csv')
    titles = hn["title"]

    pattern = r"\b[Cc]\b[^\.\+]"
    first_ten = first_10_matches(titles, pattern)
    print(first_ten)


if __name__ == '__main__':
    main()
