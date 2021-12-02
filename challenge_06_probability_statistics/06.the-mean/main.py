import pandas as pd
import matplotlib.pyplot as plt


def mean(distribution):
    return sum(distribution) / len(distribution)


# - Check whether the population mean of the population [3, 7, 2] is equal to the mean of all the sample means of size
#   2 that we can get if we do sampling without replacement.
#   - Compute the mean for each sample.
#   - Compute the mean of all the sample means. Compare it with the population mean using the == operator, and assign
#     the result of the comparison to a variable named unbiased.
def main():
    population = [3, 7, 2]

    parameter = sum(population) / len(population)

    statistics = []
    for v1 in population:
        statistics += [sum([v1, v2]) / 2 for v2 in population]

    statistic = sum(statistics) / len(statistics)

    assert statistic == parameter


if __name__ == '__main__':
    main()
