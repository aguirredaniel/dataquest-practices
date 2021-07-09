import numpy as np


# 1. Using the original taxi ndarray, calculate how many trips had JFK Airport as their destination:
#   - Use boolean indexing to select only the rows where the dropoff_location_code column (column index 6) has a value
#     that corresponds to JFK. Assign the result to jfk.
#   - Calculate how many rows are in the new jfk array and assign the result to jfk_count.
# 2. Calculate how many trips from taxi had Laguardia Airport as their destination:
#   - Use boolean indexing to select only the rows where the dropoff_location_code column (column index 6) has a value
#     that corresponds to Laguardia. Assign the result to laguardia.
#   - Calculate how many rows are in the new laguardia array. Assign the result to laguardia_count.
# 3. Calculate how many trips from taxi had Newark Airport as their destination:
#   - Select only the rows where the dropoff_location_code column has a value that corresponds to Newark, and assign the
#     result to newark.
#   - Calculate how many rows are in the new newark array and assign the result to newark_count.
def main():
    taxi = np.genfromtxt('../nyc_taxis.csv', delimiter=',', skip_header=1)

    jfk = taxi[:, 6] == 2
    jfk_count = taxi[jfk].shape[0]

    laguardia = taxi[:, 6] == 3
    laguardia_count = taxi[laguardia].shape[0]

    newark = taxi[:, 6] == 5
    newark_count = taxi[newark].shape[0]

    print(jfk_count, laguardia_count, newark_count, sep='\n')


if __name__ == "__main__":
    main()
