import numpy as np


# 1. The value at column index 5 (pickup_location) of row index 1066 is incorrect. Use assignment to change this value
#    to 1 in the taxi_modified ndarray.
# 2. The first column (index 0) contains year values as four digit numbers in the format YYYY (2016, since all trips in
#    our data set are from 2016). Use assignment to change these values to the YY format (16) in the taxi_modified ndarray.
# 3. The values at column index 7 (trip_distance) of rows index 550 and 551 are incorrect. Use assignment to change
#    these values in the taxi_modified ndarray to the mean value for that column.
def main():
    taxi = np.genfromtxt('../nyc_taxis.csv', delimiter=',', skip_header=1)
    taxi_modified = taxi.copy()
    taxi_modified[1066, 5] = 1
    taxi_modified[:, 0] = 16
    taxi_modified[[550, 551], 7] = taxi_modified[:, 7].mean()


if __name__ == "__main__":
    main()
