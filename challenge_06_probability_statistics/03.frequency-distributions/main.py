import pandas as pd


# - Generate a frequency distribution table for the Age variable, which is measured on a ratio scale, and sort the table
#   by unique values.
# - Sort the table by unique values in an ascending order, and assign the result to a variable named age_ascending.
# - Sort the table by unique values in a descending order, and assign the result to a variable named age_descending.
# - How many players are under 20?
# - How many players are 30 or over?
def main():
    pd.options.display.max_rows = 200
    pd.options.display.max_columns = 50

    wnba = pd.read_csv('../data/wnba.csv')

    freq_distro_age = wnba['Age'].value_counts()
    age_ascending = freq_distro_age.sort_index()
    age_descending = freq_distro_age.sort_index(ascending=False)

    print(age_ascending, age_descending, sep='\n')

    players_under_20 = 0
    players_are_or_over_30 = 38

    assert players_under_20 == freq_distro_age[freq_distro_age.index < 20].sum()
    assert players_are_or_over_30 == freq_distro_age[freq_distro_age.index >= 30].sum()


if __name__ == '__main__':
    main()
