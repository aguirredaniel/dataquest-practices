import pandas as pd
import matplotlib.pyplot as plt


# - Calculate the number of rows where Years since joining is accurate.
#   - Since this challenge was created in 2015, use that as the reference year.
#   - We want to know for how many rows Years since joining was correctly calculated as the Year value subtracted from
#     2015.
#   - Assign the integer value describing the number of rows with a correct value for Years since joining to
#     joined_accuracy_count.
def main():
    avengers = pd.read_csv("avengers.csv")

    true_avengers = avengers[avengers['Year'] >= 1960].copy()

    deaths = true_avengers[['Death1', 'Death2', 'Death3', 'Death4', 'Death5']].applymap(
        lambda d: 1 if d == 'YES' else 0).sum(axis=1)

    true_avengers['Deaths'] = deaths

    joined_accuracy_count = true_avengers[
        (2015 - true_avengers['Year']) == true_avengers['Years since joining']].shape[0]

    print(joined_accuracy_count)


if __name__ == '__main__':
    main()
