import pandas as pd


# - Using only the data we have in the houses_per_year data set, compute the sum of prices for each year.
# - Add all the sums together.
# - Divide the final sum by the total number of houses sold. Assign the result to a variable named weighted_mean.
# - Compute again the mean of the SalePrice column in the houses data set. Assign the value to a variable named
#   mean_original.
# - Round each mean value to 10 decimal places to get rid of minor rounding errors and then measure the difference
#   between the two means. Assign the result to a variable named difference. If the two means are equal, you should get
#   a difference of 0.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')
    houses_per_year_data = {
        'Year': [2006, 2007, 2008, 2009, 2010],
        'Mean Price': [181761.648000, 185138.207493, 178841.750804, 181404.567901, 172597.598240],
        'Houses Sold': [625, 694, 622, 648, 341]
    }

    houses_per_year = pd.DataFrame(houses_per_year_data)

    sums_price_year = (houses_per_year['Mean Price'] * houses_per_year['Houses Sold']).sum()
    weighted_mean = sums_price_year / houses_per_year['Houses Sold'].sum()

    mean_original = houses['SalePrice'].mean()
    difference = round(mean_original) - round(weighted_mean)

    print(difference)


if __name__ == '__main__':
    main()
