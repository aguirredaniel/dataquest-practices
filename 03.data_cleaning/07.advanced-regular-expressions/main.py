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


# - Uncomment the regular expression pattern. Add names to each capture group:
#   - The first capture group should be called protocol.
#   - The second capture group should be called domain.
#  - The third capture group should be called path.
# - Use the regular expression pattern to extract three named columns of url components from the url column of the hn
#   dataframe. Assign the result to url_parts
def main():
    hn = pd.read_csv('hacker_news.csv')
    pattern = r"(?P<protocol>https?)://(?P<domain>[\w\.\-]+)/?(?P<path>.*)"
    url_parts = hn['url'].str.extract(pattern, expand=False, flags=re.I)
    print(url_parts)


if __name__ == '__main__':
    main()
