import numpy as np


# 1. Calculate the number of rides in the taxi ndarray that are from February:
# 2. Create a boolean array, february_bool, that evaluates whether the items in pickup_month are equal to 2.
# 3. Use the february_bool boolean array to index pickup_month. Assign the result to february.
# 4. Use the ndarray.shape attribute to find the number of items in february. Assign the result to february_rides.
def main():
    taxi = np.genfromtxt('../nyc_taxis.csv', delimiter=',', skip_header=1)
    pickup_month = taxi[:, 1]

    february_bool = pickup_month == 2
    february = pickup_month[february_bool]
    february_rides = february.shape[0]

    print(february_rides)


if __name__ == "__main__":
    main()
