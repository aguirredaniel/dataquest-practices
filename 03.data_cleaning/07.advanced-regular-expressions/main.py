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


# - Use a regular expression to replace each of the matches in email_variations with "email" and assign the result to
#   email_uniform.
#   - You may need to iterate several times when writing your regular expression in order to match every item.
# - Use a regular expression to replace all mentions of email in titles with "email". Assign the result to titles_clean.
#   - Note that passing the cases in email_variations does not guarantee passing all the cases in the titles column.
def main():
    hn = pd.read_csv('hacker_news.csv')
    titles = hn["title"]

    email_variations = pd.Series(['email', 'Email', 'e Mail',
                                  'e mail', 'E-mail', 'e-mail',
                                  'eMail', 'E-Mail', 'EMAIL'])

    pattern = r'\be-?\s?mail'
    email_uniform = email_variations.str.replace(pattern, 'email', flags=re.IGNORECASE)

    titles_clean = titles.str.replace(pattern, 'email', flags=re.IGNORECASE)


if __name__ == '__main__':
    main()
