import pandas as pd
import re


# - Initialize a variable python_mentions with the integer value 0.
# - Create a string — pattern — containing a regular expression pattern that uses a set to match Python or python.
# - Use a loop to iterate over each item in the titles list, and for each item:
#   - Use the re.search() function to check whether pattern matches the title.
#   - If re.search() returns a match object, increment (add 1 to) the python_mentions variable.
def main():
    hn = pd.read_csv('hacker_news.csv')
    titles = hn["title"].tolist()

    python_mentions = 0
    pattern = '[Pp]ython'

    for title in titles:
        if re.search(pattern, title):
            python_mentions += 1


if __name__ == '__main__':
    main()
