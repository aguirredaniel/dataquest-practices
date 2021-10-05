import pandas as pd
import re


# - Use a regular expression and Series.str.contains() to create a boolean mask that matches items from titles
#   containing email or e-mail. Assign the result to email_bool.
# - Use email_bool to count the number of titles that matched the regular expression. Assign the result to email_count.
# - Use email_bool to select only the items from titles that matched the regular expression. Assign the result to
#   email_titles.
def main():
    hn = pd.read_csv('hacker_news.csv')
    titles = hn["title"]

    pattern = 'e-?mail'
    email_bool = titles.str.contains(pattern)
    email_count = email_bool.sum()
    email_titles = titles[email_bool]

    print(email_count, email_titles, sep='\n')


if __name__ == '__main__':
    main()
