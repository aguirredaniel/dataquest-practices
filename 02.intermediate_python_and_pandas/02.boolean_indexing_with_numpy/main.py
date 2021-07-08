import numpy as np


# 1. Create a boolean array, tip_bool, that determines which rows have values for the tip_amount column of more than 50.
# 2. Use the tip_bool array to select all rows from taxi with values tip amounts of more than 50, and the columns from
#    indexes 5 to 13 inclusive. Assign the resulting array to top_tips.
def main():
    taxi = np.genfromtxt('../nyc_taxis.csv', delimiter=',', skip_header=1)
    tip_amount = taxi[:, 12]
    tip_bool = tip_amount > 50
    top_tips = taxi[tip_bool, 5:14]

    print(top_tips)


if __name__ == "__main__":
    main()
