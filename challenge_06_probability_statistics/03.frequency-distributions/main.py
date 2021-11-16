import pandas as pd


# - Using the Series.value_counts() method, generate frequency distribution tables for the following columns:
# - Pos. Assign the frequency distribution table to a variable named freq_distro_pos.
# - Height. Assign the frequency distribution table to a variable named freq_distro_height.
def main():
    pd.options.display.max_rows = 200
    pd.options.display.max_columns = 50

    wnba = pd.read_csv('../data/wnba.csv')

    freq_distro_pos = wnba['Pos'].value_counts()
    freq_distro_height = wnba['Height'].value_counts()

    print(freq_distro_pos, freq_distro_height, sep='\n')


if __name__ == '__main__':
    main()
