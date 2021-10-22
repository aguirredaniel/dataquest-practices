from challenge_03_data_cleaning.nyc_high_school_data import read_data, make_initial_clean, merge_data

import matplotlib.pyplot as plt


# - Create a scatterplot of total_enrollment (on the horizontal axis) versus sat_score (on the vertical axis).
def main():
    data = read_data()
    data = make_initial_clean(data)
    combined = merge_data(data)

    correlations = combined.corr()['sat_score']

    low_enrollment = combined[(combined['total_enrollment'] < 1000) & (combined['sat_score'] < 1000)]
    print(low_enrollment['School Name'])


if __name__ == '__main__':
    main()
