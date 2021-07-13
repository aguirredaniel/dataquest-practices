import numpy as np


# 1. Create a new ndarray, cleaned_taxi, containing only rows for which the values of trip_mph are less than 100.
# 2. Calculate the mean of the trip_distance column of cleaned_taxi. Assign the result to mean_distance.
# 3. Calculate the mean of the trip_length column of cleaned_taxi. Assign the result to mean_length.
# 4. Calculate the mean of the total_amount column of cleaned_taxi. Assign the result to mean_total_amount.
def main():
    taxi = np.genfromtxt('../nyc_taxis.csv', delimiter=',', skip_header=1)
    trip_mph = taxi[:, 7] / (taxi[:, 8] / 3600)
    cleaned_taxi = taxi[trip_mph < 100]
    mean_distance = cleaned_taxi[:, 7].mean()
    mean_length = cleaned_taxi[:, 8].mean()
    mean_total_amount = cleaned_taxi[:, 13].mean()


if __name__ == "__main__":
    main()
