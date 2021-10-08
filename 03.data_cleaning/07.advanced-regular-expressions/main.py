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


# - Write a regular expression to match cases of repeated words:
#   - We'll define a word as a series of one or more word characters preceded and followed by a boundary anchor.
#   - We'll define repeated words as the same word repeated twice, separated by a single whitespace character.
# - Select only the items in titles that match the regular expression. Assign the result to repeated_words.
def main():
    hn = pd.read_csv('hacker_news.csv')
    titles = hn["title"]

    pattern = r'\b(\w+)\s\1\b'
    repeated_word = titles[titles.str.contains(pattern)]

    print(repeated_word)


if __name__ == '__main__':
    main()
