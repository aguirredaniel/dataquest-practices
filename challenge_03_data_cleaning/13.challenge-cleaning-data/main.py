import pandas as pd
import matplotlib.pyplot as plt


# - Create a new column, Deaths, that contains the number of times each superhero died. The possible values for each
#   death field are YES, NO, and NaN for missing data.
#   - Keep all of the original columns (including Death1 to Death5) and update true_avengers with the new Deaths column.
def main():
    avengers = pd.read_csv("avengers.csv")

    true_avengers = avengers[avengers['Year'] >= 1960].copy()

    deaths = true_avengers[['Death1', 'Death2', 'Death3', 'Death4', 'Death5']].applymap(
        lambda d: 1 if d == 'YES' else 0).sum(axis=1)

    true_avengers['Deaths'] = deaths

    print(true_avengers['Deaths'])


if __name__ == '__main__':
    main()
