import numpy as np


def main():
    taxi = np.genfromtxt('../nyc_taxis.csv', delimiter=',', skip_header=1)
    taxi_shape = taxi.shape

    print(taxi_shape)


if __name__ == "__main__":
    main()
