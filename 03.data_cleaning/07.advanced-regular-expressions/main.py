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


# -Create a new column called flavor in the hn_sql dataframe, containing extracted mentions of SQL flavors, defined as:
#   - Any time 'SQL' is preceded by one or more word characters.
#   - Ignoring all case variation.
# - Use the Series.str.lower() method to clean the values in the flavor column by converting them to lowercase. Assign
#   the values back to the column in hn_sql.
# - Use the DataFrame.pivot_table() method to create a pivot table, sql_pivot.
#   - The index of the pivot table should be the flavor column.
#   - The values of the pivot table should be the mean of the num_comments column, aggregated by SQL flavor.
def main():
    hn = pd.read_csv('hacker_news.csv')
    titles = hn["title"]

    pattern = r"\w+SQL"
    hn_sql = hn[titles.str.contains(pattern, flags=re.I)].copy()
    pattern = r"(\w+SQL)"
    hn_sql['flavor'] = hn_sql['title'].str.extract(pattern, flags=re.I)
    hn_sql['flavor'] = hn_sql['flavor'].str.lower()

    sql_pivot = hn_sql.pivot_table(index='flavor', values='num_comments', aggfunc=np.mean)

    print(sql_pivot)


if __name__ == '__main__':
    main()
