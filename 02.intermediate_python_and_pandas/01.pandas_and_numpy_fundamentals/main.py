import csv
import numpy as np


def _process_file_as_np_array(file_name) -> np.array:
    """  Read a csv file and return as ndarray (dataset).

    Args:
        file_name: A string name of file to be read.

    Returns:
        A ndarray that represent a dataset.

        For example:
        For file with this content
        a,b,c,d
        e,f,g,h
        i,j,k,l

        returns ndarray
        [['a','b','c','d']
         ['e','f','g','h']
         ['i','j','k','l']]
    """
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        taxi_list = list(reader)
        taxi_list = taxi_list[1:]
        converted_taxi_list = []
        for row in taxi_list:
            converted_row = []
            for item in row:
                converted_row.append(float(item))
            converted_taxi_list.append(converted_row)
        return np.array(converted_taxi_list)


# 1. Use vector division to divide trip_distance_miles by trip_length_hours. Assign the result to trip_mph.
# 2. After you run your code, use the variable inspector below the code box to inspect the contents of the
#    new trip_mph variable.
def main():
    taxi = _process_file_as_np_array('nyc_taxis.csv')
    trip_distance_miles = taxi[:, 7]
    trip_length_seconds = taxi[:, 8]
    trip_length_hours = trip_length_seconds / 3600
    trip_mph = trip_distance_miles / trip_length_hours

    print(trip_distance_miles, trip_length_seconds, trip_length_hours, trip_mph, sep='\n')


if __name__ == "__main__":
    main()
