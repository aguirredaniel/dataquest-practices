from challenge_03_data_cleaning.nyc_high_school_data import read_data, make_initial_clean, merge_data
import matplotlib.pyplot as plt


# - Find the average values for each column for each school_dist in combined.
#   - Use the pandas.DataFrame.groupby() method to group combined by school_dist.
#   - Use the agg() method, along with the numpy.mean function as an argument to calculate the average of each group.
#   - Assign the result to the variable districts.
# - Reset the index of districts, making school_dist a column again.
#   - Use the pandas.DataFrame.reset_index() method with the keyword argument inplace=True.
# - Display the first few rows of districts to verify that everything went okay.
def main():
    data = read_data()
    data = make_initial_clean(data)
    combined = merge_data(data)

    districts = combined.groupby(by='school_dist').mean()
    districts.reset_index(inplace=True)
    print(districts.head())


if __name__ == '__main__':
    main()
