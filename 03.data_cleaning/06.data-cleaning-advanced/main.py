import pandas as pd
import re


# - Write a regular expression, assigning it as a string to the variable pattern. The regular expression should match,
#   in order:
#   - A single open bracket character.
#   - One or more word characters.
#   - A single close bracket character.
#  - Use the regular expression to select only items from titles that match. Assign the result to the variable
#    tag_titles.
# - Count how many matching titles there are. Assign the result to tag_count.
def main():
    hn = pd.read_csv('hacker_news.csv')
    titles = hn["title"]

    pattern = r'\[\w+\]'
    tag_bool = titles.str.contains(pattern)
    tag_count = tag_bool.sum()
    tag_titles = titles[tag_bool]

    print(tag_count, tag_titles, sep='\n')


if __name__ == '__main__':
    main()
