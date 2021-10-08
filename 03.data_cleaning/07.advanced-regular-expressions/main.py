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


# - Write a regular expression that extracts URL components using three capture groups:
#   - The first capture group should include the protocol text, up to but not including ://.
#   - The second group should contain the domain, from after :// up to but not including /.
#   - The third group should contain the page path, from after / to the end of the string.
# - Use the regular expression pattern to extract the URL components from the test_urls series. Assign the results to
#   test_url_parts.
# - Use the regular expression pattern to extract the URL components from the url column of the hn dataframe. Assign the
#   results to url_parts.
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

    pattern = r'(https?):\/{2}([\w\.-]+)/?(.*)'
    test_url_parts = test_urls.str.extract(pattern, expand=False, flags=re.I)
    url_parts = hn['url'].str.extract(pattern, expand=False, flags=re.I)


if __name__ == '__main__':
    main()
