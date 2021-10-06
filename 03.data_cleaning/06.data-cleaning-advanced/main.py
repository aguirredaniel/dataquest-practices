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


# - Write a regular expression that will match titles containing Java.
#   - You might like to use the first_10_matches() function or a site like RegExr to build your regular expression.
#   - The regex should match whether or not the first character is capitalized.
#   - The regex shouldn't match where 'Java' is followed by the letter 'S' or 's'.
# - Select every row from titles that match the regular expression. Assign the result to java_titles.
def main():
    hn = pd.read_csv('hacker_news.csv')
    titles = hn["title"]

    pattern = r'[Jj]ava[^Ss]'
    java_titles = titles[titles.str.contains(pattern)]
    print(java_titles)


if __name__ == '__main__':
    main()
