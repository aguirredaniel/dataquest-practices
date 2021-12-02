import pandas as pd
import matplotlib.pyplot as plt


def mean(distribution):
    return sum(distribution) / len(distribution)


# -Take 10000 samples of sample size 100 from the population of sale prices and measure the mean of each sample. For each of the 10000 iterations of a for loop:
#
# Use Series.sample() to take a sample of size 100 from the SalePrice variable. The random_state parameter is 0 for the first iteration, 1 for the second iteration, 2 for the third iteration, and so on.
# Compute the mean of the sample.
# Use plt.hist() to generate a histogram to visualize the distribution of sample means.
#
# Draw a vertical line for the population mean.
# Label the x-axis "Sample mean".
# Label the y-axis "Frequency".
# Set the range of the x-axis to (0,500000). This is the same range as the histogram we built above has. Can you observe any obvious difference between the two histograms now that we've increased the sample size?
def main():
    houses = pd.read_csv('AmesHousing_1.txt', sep='\t')
    sale_price = houses['SalePrice']
    parameter = sale_price.mean()
    statistics = [sale_price.sample(n=100, random_state=i).mean() for i in range(10000)]

    plt.hist(statistics)
    plt.xlabel('Sample mean')
    plt.ylabel('Frequency')
    plt.axvline(parameter)

    plt.xlim((0, 500000))
    plt.show()


if __name__ == '__main__':
    main()
