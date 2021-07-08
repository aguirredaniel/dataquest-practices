import numpy as np


# 1. Evaluate whether the elements in array a are less than 3. Assign the result to a_bool.
# 2. Evaluate whether the elements in array b are equal to "blue". Assign the result to b_bool.
# 3. Evaluate whether the elements in array c are greater than 100. Assign the result to c_bool.
def practice_boolean_arrays():
    a = np.array([1, 2, 3, 4, 5])
    b = np.array(["blue", "blue", "red", "blue"])
    c = np.array([80.0, 103.4, 96.9, 200.3])

    a_bool = a < 3
    b_bool = b == "blue"
    c_bool = c >= 100

    print(a_bool, b_bool, c_bool, sep='\n')

def main():
    taxi = np.genfromtxt('../nyc_taxis.csv', delimiter=',', skip_header=1)
    taxi_shape = taxi.shape

    print(taxi_shape)


if __name__ == "__main__":
    practice_boolean_arrays()
