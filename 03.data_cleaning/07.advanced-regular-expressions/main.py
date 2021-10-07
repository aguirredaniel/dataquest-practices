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


# - Write a regular expression and assign it to pattern. The regular expression should:
#   - Match instances of C or c where they are not preceded or followed by another word character.
#   - From the match above:
#     - Exclude instances where it is followed by a . or + character, without removing instances where the match occurs
#       at the end of the sentence.
#     - Exclude instances where the word 'Series' immediately precedes the match.
# - Count how many stories in titles match the regular expression. Assign the result to c_mentions.
def main():
    hn = pd.read_csv('hacker_news.csv')
    titles = hn["title"]

    pattern = r"(?<!Series\s)\b[Cc]\b(?![\+\.])"
    c_mentions = titles.str.contains(pattern).sum()
    print(c_mentions)


if __name__ == '__main__':
    main()
