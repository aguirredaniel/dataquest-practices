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


# - Write a regular expression to extract the domains from test_urls and assign the result to test_urls_clean. We
#   suggest the following technique:
#    - Using a series of characters that will match the protocol.
#   - Inside a capture group, using a set that will match the character classes used in the domain.
#   - Because all of the URLs either end with the domain, or continue with page path which starts with / (a character
#     not found in any domains), we don't need to cater for this part of the URL in our regular expression.
# - Use a regular expression to extract the domains from the url column of the hn dataframe. Assign the result to
#   domains.
#   - Note that passing the cases in test_urls does not guarantee passing all the cases in the url column.
# - Use Series.value_counts() to build a frequency table of the domains in domains, limiting the frequency table to just
#   to the top 5. Assign the result to top_domains.
def main():
    hn = pd.read_csv('hacker_news.csv')
    test_urls = pd.Series([
        'https://www.amazon.com/Technology-Ventures-Enterprise-Thomas-Byers/dp/0073523429',
        'http://www.interactivedynamicvideo.com/',
        'http://www.nytimes.com/2007/11/07/movies/07stein.html?_r=0',
        'http://evonomics.com/advertising-cannot-maintain-internet-heres-solution/',
        'HTTPS://github.com/keppel/pinn',
        'Http://phys.org/news/2015-09-scale-solar-youve.html',
        'https://iot.seeed.cc',
        'http://www.bfilipek.com/2016/04/custom-deleters-for-c-smart-pointers.html',
        'http://beta.crowdfireapp.com/?beta=agnipath',
        'https://www.valid.ly?param',
        'http://css-cursor.techstream.org'
    ])

    pattern = 'https?:\/{2}([w{3}\.]?[\w\.-]+)'
    test_urls_clean = test_urls.str.extract(pattern, expand=False, flags=re.I)
    domains = hn['url'].str.extract(pattern, expand=False, flags=re.I)

    top_domains = domains.value_counts().head()

    print(test_urls_clean, top_domains, sep='\n')


if __name__ == '__main__':
    main()
