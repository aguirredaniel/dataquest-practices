from numpy.random import randint, seed


# - Generate 5000 different distributions, measure the total distances above and below the mean, and check whether they
#   are equal. For each of the 5000 iterations of a for loop:
#   - Set a seed using the seed() function from numpy.random. For the first iteration, the seed number should be 0, for
#     the second iteration it should be 1, for the third it should be 2, and so on.
#   - Generate randomly a distribution of integers using the randint() function from numpy.random. Pass the right
#     arguments to randint() such that each distribution will:
#     - Have 10 values.
#     - The values can range from 0 to 1000.
#   - Compute the mean of the distribution.
#   - Measure the total distance above and below the mean.
#     - Round off each distance to 1 decimal place using the round() function. This will prevent rounding errors at the
#       13th or 14th decimal place.
#   - Compare the two sums. If they are equal, then increment a variable named equal_distances with 1. You'll need to
#     define equal_distances outside the loop with a value of 0.
# - At the end equal_distances should have a value of 5000. This will confirm that for each of the 5000 distributions
#   the total distance of the values above the mean is equal to the total distance of the values below the mean.
def main():
    equal_distances = 0
    for i in range(5000):
        seed(i)
        distribution = randint(0, 100, 10)
        mean = sum(distribution) / len(distribution)
        below_differences = (mean - value for value in distribution if value < mean)
        above_differences = (value - mean for value in distribution if value > mean)

        if round(sum(below_differences), 1) == round(sum(above_differences), 1):
            equal_distances += 1

    print(equal_distances)


if __name__ == '__main__':
    main()
