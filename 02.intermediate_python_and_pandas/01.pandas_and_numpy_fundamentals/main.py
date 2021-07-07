import csv
import numpy as np


# 1. Add a line of code using the numpy.array() constructor to convert the converted_taxi_list variable to a NumPy ndarray.
# 2. Assign the result to the variable name taxi.

def main():
    with open('nyc_taxis.csv', 'r') as file:
        reader = csv.reader(file)
        taxi_list = list(reader)
        taxi_list = taxi_list[1:]
        converted_taxi_list = []
        for row in taxi_list:
            converted_row = []
            for item in row:
                converted_row.append(float(item))
            converted_taxi_list.append(converted_row)
        taxi = np.array(converted_taxi_list)
        print(taxi)


if __name__ == "__main__":
    main()
