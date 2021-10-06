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


# - Count the number of times that a tag (e.g. [pdf] or [video]) occurs at the start of a title in titles. Assign the
#   result to beginning_count.
# - Count the number of times that a tag (e.g. [pdf] or [video]) occurs at the end of a title in titles. Assign the
#   result to ending_count.
def main():
    hn = pd.read_csv('hacker_news.csv')
    titles = hn["title"]

    beginning_count = titles.str.contains(r'^\[\w+\]').sum()
    ending_count = titles.str.contains(r'\[\w+\]$').sum()

    print(beginning_count, ending_count, sep='\n')


if __name__ == '__main__':
    main()
