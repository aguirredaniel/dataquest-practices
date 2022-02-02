import numpy as np
import matplotlib.pyplot as plt


# - Inside a for loop that repeats 1000 times:
# - Use the numpy.random.random function to generate 32561 numbers between 0.0 and 1.0.
# - Pass (32561,) into the numpy.random.random function to get a vector with 32561 elements.
# - For each of the numbers, if it is less than .5, replace it with 0, otherwise replace it with 1.
# - Count up how many times 0 occurs (Male frequency), and how many times 1 occurs (Female frequency).
# - Use the expected frequencies from earlier to compute the chi-squared value.
# - Compute male_diff by subtracting the expected Male count from the observed Male count, squaring it, and dividing by
#   the expected Male count.
# - Compute female_diff by subtracting the expected Female count from the observed Female count, squaring it, and
#   dividing by the expected Female count.
# - Add up male_diff and female_diff to get the chi-squared value.
# - Append the chi-squared value to chi_squared_values.
# - Create a histogram with chi_squared_values using the plt.hist method.
# - For answer checking purposes, do not use plt.show() here.
def main():
    female_diff = (10771 - 16280.5) ** 2 / 16280.5
    male_diff = (21790 - 16280.5) ** 2 / 16280.5
    gender_chisq = female_diff + male_diff

    chi_squared_values = []
    np.random.seed(1)
    for _ in range(1000):
        frequency = {0: 0, 1: 0}
        for v in np.random.random(32561, ):
            if v < 0.5:
                frequency[0] += 1
            else:
                frequency[1] += 1

        female_diff = (frequency[0] - 16280.5) ** 2 / 16280.5
        male_diff = (frequency[1] - 16280.5) ** 2 / 16280.5
        gender_chisq = female_diff + male_diff
        chi_squared_values.append(gender_chisq)

    plt.hist(chi_squared_values)
    plt.show()


if __name__ == '__main__':
    main()
