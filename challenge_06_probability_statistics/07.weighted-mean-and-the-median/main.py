import pandas as pd


# - Compute the mean of the Mean Price column in the houses_per_year data set. Assign the value to a variable named
#   mean_new.
#   - Note that houses_per_year is a DataFrame object, so you can use directly the Series.mean() method.
# - Compute the mean of the SalePrice column in the houses data set. Assign the value to a variable named mean_original.
# - Measure the difference between the two means, and assign the result to a variable named difference. If they are
#   equal, the difference should be 0.
#   - For answer checking purposes use mean_original - mean_new, not mean_new - mean_original.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')
    houses_per_year_data = {
        'Year': [2006, 2007, 2008, 2009, 2010],
        'Mean Price': [181761.648000, 185138.207493, 178841.750804, 181404.567901, 172597.598240],
        'Houses Sold': [625, 694, 622, 648, 341]
    }

    houses_per_year = pd.DataFrame(houses_per_year_data)

    mean_new = houses_per_year['Mean Price'].mean()
    mean_original = houses['SalePrice'].mean()
    difference = mean_original - mean_new

    print(difference)

if __name__ == '__main__':
    main()
