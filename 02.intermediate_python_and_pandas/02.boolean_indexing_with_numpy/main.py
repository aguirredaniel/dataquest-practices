import numpy as np


# 1. In our new column at index 15, assign the value 1 if the pickup_location_code (column index 5) corresponds to an
#    airport location, leaving the value as 0 otherwise by performing these three operations:
# 2. For rows where the value for the column index 5 is equal to 2 (JFK Airport), assign the value 1 to column index 15.
# 3. For rows where the value for the column index 5 is equal to 3 (LaGuardia Airport), assign the value 1 to column
#    index 15.
# 4. For rows where the value for the column index 5 is equal to 5 (Newark Airport), assign the value 1 to column
#    index 15.
def main():
    taxi = np.genfromtxt('../nyc_taxis.csv', delimiter=',', skip_header=1)
    # create a new column filled with `0`.
    zeros = np.zeros([taxi.shape[0], 1])
    taxi_modified = np.concatenate([taxi, zeros], axis=1)

    taxi_modified[taxi_modified[:, 5] == 2, 15] = 1
    taxi_modified[taxi_modified[:, 5] == 3, 15] = 1
    taxi_modified[taxi_modified[:, 5] == 5, 15] = 1


if __name__ == "__main__":
    main()
