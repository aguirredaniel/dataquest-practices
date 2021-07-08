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


# Check if the sum of each row in fare_components equals the value in the total_amount column.

# 1. Use the ndarray.sum() method to calculate the sum of each row in fare_components. Assign the result to fare_sums.
# 2. Extract the 14th column in taxi_first_five. Assign to fare_totals.
# 3. Print fare_totals and fare_sums. Use the variable inspector to verify that the results match.

def main():
    taxi = _process_file_as_np_array('nyc_taxis.csv')
    taxi_first_five = taxi[:5]
    fare_components = taxi_first_five[:, 9:13]

    fare_sums = fare_components.sum(axis=1)
    fare_totals = taxi_first_five[:, 13]

    print(fare_sums, fare_totals, sep='\n')


if __name__ == "__main__":
    main()
