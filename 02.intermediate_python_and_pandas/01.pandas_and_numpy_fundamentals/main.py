import csv
import numpy as np


def _process_file_as_np_array(file_name) -> np.array:
    """  Read a csv file and return as ndarray (dataset).

    Args:
        file_name: A string name of file to be readed.

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


# 1. Select the row at index 0. Assign it to row_0.
# 2. Select every column for the rows at indices 391 to 500 inclusive. Assign them to rows_391_to_500.
# 3. Select the item at row index 21 and column index 5. Assign it to row_21_column_5.
def main():
    taxi = _process_file_as_np_array('nyc_taxis.csv')
    row_0 = taxi[0]
    rows_391_to_500 = taxi[391:501]
    row_21_column_5 = taxi[21, 5]


if __name__ == "__main__":
    main()
