import pandas as pd
import matplotlib.pyplot as plt


# - Generate a histogram for the casual column.
# - Try to make a few quick observations about the histogram.
#   - What's the approximate range?
#   - What's the interval with the greatest frequency?
#   - What's the interval with the lowest frequency?
# - Compare the shape of the casual histogram with the shape of the histogram we generated for the cnt column. What
#   differences do you notice?
def main():
    bike_sharing = pd.read_csv('../day.csv')
    bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

    plt.hist(bike_sharing['casual'])
    plt.show()


if __name__ == '__main__':
    main()
