import pandas as pd
import matplotlib.pyplot as plt


def mean(distribution):
    return sum(distribution) / len(distribution)


# - For each iteration of a for loop that iterates 101 times:
#
# Sample the SalePrice distribution using the Series.sample() method.
# For the first iteration, the random_state parameter is 0, for the second iteration is 1, for the third is 2, and so on.
# For the first iteration, the sample size is 5.
# The last sample size is 2905 (which is close to 2930, the population's size).
# To achieve that, you'll need to increment the sample size by 29 for every new iteration. Note that you'll first have to define the sample size with a value of 5 outside the loop.
# Compute the sample mean.
# Compute the sampling error. For answer checking purposes, use parameter - static
# Generate a scatter plot to represent visually how the sampling error changes as the sample size increases.
#
# Place the sample sizes on the x-axis.
# Place the sampling errors on the y-axis.
# Use plt.axhline() to generate a horizontal line at 0 to illustrate the point where the sampling error is 0.
# Use plt.axvline() to generate a vertical line at 2930 to illustrate the population size.
# Label the x-axis "Sample size".
# Label the y-axis "Sampling error".
def main():
    houses = pd.read_csv('AmesHousing_1.txt', sep='\t')

    parameter = houses['SalePrice'].mean()
    sample_size = 5

    sample_sizes = []
    sampling_errors = []
    for i in range(101):
        sample = houses['SalePrice'].sample(n=sample_size, random_state=i)

        static = sample.mean()
        sampling_error = parameter - static

        sample_sizes.append(sample_size)
        sampling_errors.append(sampling_error)

        sample_size += 29

    plt.scatter(x=sample_sizes, y=sampling_errors)
    plt.axhline(0)
    plt.axvline(2930)
    plt.xlabel('Sample size')
    plt.ylabel('Sampling error')

    plt.show()


if __name__ == '__main__':
    main()
