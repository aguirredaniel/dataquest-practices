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


# - Generate a frequency distribution table for the transformed PTS_ordinal_scale column.
# - Order the table by unique values in a descending order (not alphabetically).
# - Assign the result to a variable named pts_ordinal_desc.
def main():
    pd.options.display.max_rows = 200
    pd.options.display.max_columns = 50

    wnba = pd.read_csv('../data/wnba.csv')
    wnba['PTS_ordinal_scale'] = wnba.apply(make_pts_ordinal, axis=1)
    freq_distro_pts_ordinal = wnba['PTS_ordinal_scale'].value_counts()
    print(freq_distro_pts_ordinal)

    pts_ordinal_desc = freq_distro_pts_ordinal.iloc[[4, 3, 0, 2, 1, -1]]


if __name__ == '__main__':
    main()
