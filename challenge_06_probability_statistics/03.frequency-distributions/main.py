import pandas as pd


def make_pts_ordinal(row):
    if row['PTS'] <= 20:
        return 'very few points'
    if 20 < row['PTS'] <= 80:
        return 'few points'
    if 80 < row['PTS'] <= 150:
        return 'many, but below average'
    if 150 < row['PTS'] <= 300:
        return 'average number of points'
    if 300 < row['PTS'] <= 450:
        return 'more than average'
    else:
        return 'much more than average'


# - Answer the following questions about the Age variable:
# - What proportion of players are 25 years old? Assign your answer to a variable named proportion_25.
# - What percentage of players are 30 years old? Assign your answer to a variable named percentage_30.
# - What percentage of players are 30 years or older? Assign your answer to a variable named percentage_over_30.
# - What percentage of players are 23 years or younger? Assign your answer to a variable named percentage_below_23.
def main():
    pd.options.display.max_rows = 200
    pd.options.display.max_columns = 50

    wnba = pd.read_csv('../data/wnba.csv')
    wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis=1)
    freq_relative_age = wnba['Age'].value_counts(normalize=True) * 100

    proportion_25 = freq_relative_age[25] / 100
    percentage_30 = freq_relative_age[30]
    percentage_over_30 = freq_relative_age[freq_relative_age.index >= 30].sum()
    percentage_below_23 = freq_relative_age[freq_relative_age.index <= 23].sum()

    print(proportion_25, percentage_30, percentage_over_30, percentage_below_23, sep='\n')


if __name__ == '__main__':
    main()
