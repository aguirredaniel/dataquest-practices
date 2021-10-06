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

    email_tests = pd.Series(['email', 'Email', 'e Mail', 'e mail', 'E-mail',
                             'e-mail', 'eMail', 'E-Mail', 'EMAIL', 'emails', 'Emails',
                             'E-Mails'])

    pattern = r'\be-?\s?mails?\b'

    email_mentions = email_tests.str.contains(pattern, flags=re.IGNORECASE).sum()
    assert (email_mentions == email_tests.size)

    email_mentions = titles.str.contains(pattern, flags=re.IGNORECASE).sum()
    print(email_mentions)


if __name__ == '__main__':
    main()
