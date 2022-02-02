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
    expected_value = 162.805
    female_diff = (107.71 - expected_value) ** 2 / expected_value
    male_diff = (217.90 - expected_value) ** 2 / expected_value
    gender_chisq = female_diff + male_diff

    print(female_diff, male_diff, gender_chisq, sep='\n')


if __name__ == '__main__':
    main()
