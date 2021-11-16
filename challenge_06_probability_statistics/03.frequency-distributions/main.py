import pandas as pd


# - Generate a grouped frequency distribution for the MIN variable (minutes played during the season), and experiment
#   with the number of class intervals to get a sense for what conclusions you can draw as you vary the number of class
#   intervals. Try to experiment with the following numbers of class intervals:
#   -  1
#   -  2
#   -  3
#   -  5
#   - 10
#   - 15
#   - 20
#   - 40
def main():
    pd.options.display.max_rows = 200
    pd.options.display.max_columns = 50

    wnba = pd.read_csv('../data/wnba.csv')

    class_intervals = [1, 2, 3, 5, 10, 15, 20, 40]

    for class_interval in class_intervals:
        grouped_freq_table = (wnba['MIN'].value_counts(bins=class_interval, normalize=True) * 100).sort_index(
            ascending=False)
        print(grouped_freq_table)


if __name__ == '__main__':
    main()
