from challenge_03_data_cleaning.nyc_high_school_data import read_data, make_initial_clean, merge_data


# - Use the pandas.DataFrame.corr() method on the combined dataframe to find all possible correlations. Assign the
#   result to correlations.
# - Filter correlations so that it only shows correlations for the column sat_score.
# - Display all of the rows in correlations and examine them.
def main():
    data = read_data()
    data = make_initial_clean(data)
    combined = merge_data(data)

    correlations = combined.corr()['sat_score']
    print(correlations)


if __name__ == '__main__':
    main()
