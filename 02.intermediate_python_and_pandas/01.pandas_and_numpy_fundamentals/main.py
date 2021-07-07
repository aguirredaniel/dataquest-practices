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


# 1. Select every row for the columns at indices 1, 4, and 7. Assign them to columns_1_4_7.
# 2. Select the columns at indices 5 to 8 inclusive for the row at index 99. Assign them to row_99_columns_5_to_8.
# 33. Select the rows at indices 100 to 200 inclusive for the column at index 14. Assign them to rows_100_to_200_column_14.

def main():
    taxi = _process_file_as_np_array('nyc_taxis.csv')
    columns_1_4_7 = taxi[:, [1, 4, 7]]  # 2D ndarray
    row_99_columns_5_to_8 = taxi[99, 5:9]  # 1D ndarray
    rows_100_to_200_column_14 = taxi[100:201, 14]  # 1D ndarray

    print(columns_1_4_7, row_99_columns_5_to_8, rows_100_to_200_column_14, sep='\n')

if __name__ == "__main__":
    main()
