import matplotlib.pyplot as plt
import pandas as pd


# - Generate a kernel density plot for the SalePrice variable to find out how far off $220,000 is from the mean.
#
# Generate the plot using Series.plot.kde().
# The limits of the x-axis should be the minimum and the maximum value of the SalePrice variable. To set the limits you can use the xlim parameter of Series.plot.kde().
# Plot a vertical line to indicate visually the location of the mean using plt.axvline().
# The color of the line should be black, and its label should be 'Mean'. You can use the color and label parameters of plt.axvline().
# Plot a vertical line to indicate visually the standard deviation distance above the mean — you'll have to generate a vertical line for the sum of the mean and standard deviation.
# Assume that the data is a population and compute the standard deviation without using Bessel's correction.
# The color of the line should be red and its label should be 'Standard deviation'.
# Plot a vertical line for the $220,000 price.
# The color of the line should be orange and its label should be '220000'.
# Display all the labels using plt.legend().
# Examine the graph and figure out whether a price of $220,000 is very expensive. If it's very expensive, assign True to variable named very_expensive, otherwise assign False.
def main():
    houses = pd.read_csv('../data/AmesHousing_1.txt', sep='\t')

    sale = houses['SalePrice']

    sale.plot.kde(xlim=(sale.min(), sale.max()))

    plt.axvline(sale.mean(), color='black', label='Mean')
    plt.axvline(sale.std(ddof=0) + sale.mean(), color='red', label='Standard deviation')
    plt.axvline(220000, color='orange', label='220000')

    plt.legend()
    plt.show()

    very_expensive = False
    assert not very_expensive


if __name__ == '__main__':
    main()
