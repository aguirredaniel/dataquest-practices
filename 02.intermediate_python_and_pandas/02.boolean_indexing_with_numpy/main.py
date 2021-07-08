import numpy as np


# 1. Select the fourteenth column (index 13) in taxi_copy. Assign it to a variable named total_amount.
# 2. For rows where the value of total_amount is less than 0, use assignment to change the value to 0.
def main():
    taxi = np.genfromtxt('../nyc_taxis.csv', delimiter=',', skip_header=1)
    taxi_copy = taxi.copy()

    total_amount = taxi_copy[:, 13]
    total_amount[total_amount < 0] = 0


if __name__ == "__main__":
    main()
