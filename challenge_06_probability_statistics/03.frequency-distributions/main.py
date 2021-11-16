import pandas as pd
from scipy.stats import percentileofscore


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


# - What percentage of players played half the number of games or less in the 2016-2017 season (there are 34 games in
#   the WNBA’s regular season)? Use the Games Played column to find the data you need, and assign your answer to a
#    variable named percentile_rank_half_less.
# - What percentage of players played more than half the number of games of the season 2016-2017? Assign your result to
#   percentage_half_more.
def main():
    pd.options.display.max_rows = 200
    pd.options.display.max_columns = 50

    wnba = pd.read_csv('../data/wnba.csv')
    wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis=1)

    percentile_rank_half_less = percentileofscore(wnba['Games Played'], 17, kind='weak')
    percentage_half_more = 100 - percentile_rank_half_less
    print(percentile_rank_half_less, percentage_half_more, sep='\n')


if __name__ == '__main__':
    main()
