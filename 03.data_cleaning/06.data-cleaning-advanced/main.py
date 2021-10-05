import pandas as pd
import re


# - Assign the title column from the hn dataframe to the variable titles.
# - Use Series.str.contains() and Series.sum() with the provided regex pattern to count how many Hacker News titles
#   contain Python or python. Assign the result to python_mentions.
def main():
    hn = pd.read_csv('hacker_news.csv')
    titles = hn["title"]

    pattern = '[Rr]uby'
    ruby_titles = titles[titles.str.contains(pattern)]

    print(ruby_titles)


if __name__ == '__main__':
    main()
