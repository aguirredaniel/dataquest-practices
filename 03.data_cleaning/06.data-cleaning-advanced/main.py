import pandas as pd
import re


# - Use Series.str.extract() and Series.value_counts() with the modified regex pattern to produce a frequency table of
#  all the tags in the titles series. Assign the frequency table to tag_freq.
def main():
    hn = pd.read_csv('hacker_news.csv')
    titles = hn["title"]

    pattern = r'\[(\w+)\]'
    tag_freq = titles.str.extract(pattern, expand=False).value_counts()

    print(tag_freq)


if __name__ == '__main__':
    main()
