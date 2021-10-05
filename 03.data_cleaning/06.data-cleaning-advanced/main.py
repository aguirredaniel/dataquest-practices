import pandas as pd
import re


# - Assign the title column from the hn dataframe to the variable titles.
# - Use Series.str.contains() and Series.sum() with the provided regex pattern to count how many Hacker News titles
#   contain Python or python. Assign the result to python_mentions.
def main():
    hn = pd.read_csv('hacker_news.csv')
    titles = hn["title"]

    pattern = '[Pp]ython'
    python_mentions = titles.str.contains(pattern).sum()

    print(python_mentions)


if __name__ == '__main__':
    main()
