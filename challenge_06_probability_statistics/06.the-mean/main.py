# - Compute the mean of this distribution and assign the result to a variable named mean.
# - Find out whether the value of the mean is at the center of the distribution's range (0 - 13). If it is, assign True
#   to a variable named center, otherwise assign False.
# - Check whether the sum of the distances of the values that are below the mean is equal to the sum of the distances of
#   the values that are above the mean.
#   - Measure the distance of each value from the mean. You can ignore potential values that are equal to the mean
#     because the distances will be 0 for these cases.
#   - Sum up the distances of the values that are above the mean, and then sum up separately the distances of the values
#     that are below the mean.
#   - Compare the results of the two sums — if they are equal, assign True to a variable named equal_distances,
#     otherwise assign False.

def main():
    distribution = [0, 2, 3, 3, 3, 4, 13]
    mean = sum(distribution) / len(distribution)
    center = False
    equal_distances = True
    print(mean)


if __name__ == '__main__':
    main()