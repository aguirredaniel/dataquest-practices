import matplotlib.pyplot as plt
import pandas as pd


# - Find out the number of standard deviations away from the mean for a price of $220,000 in the distribution of the
#   SalePrice variable.
#   - Measure the distance between $220,000 and the mean of the SalePrice column.
#   - Divide the distance by the standard deviation of the SalePrice column (assume the data we have is a population) to
#     find the number of standard deviations away from the mean.
#     - Assign your result to a variable named st_devs_away.
#     - If you can't understand why we divide, think about this way: if we have a distance of 6 and a standard deviation
#       of 2, then that is three standard deviations away because 6 : 2 = 3 .
# - Does the number of standard deviations match our visual estimate from the last exercise?
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')

    sale = houses['SalePrice']
    mean = sale.mean()
    std = sale.std(ddof=0)
    price = 220000
    st_devs_away = abs(mean - price) / std

    print(st_devs_away)

if __name__ == '__main__':
    main()
