import pandas as pd
import matplotlib.pyplot as plt


# - We only want to keep the Avengers who were introduced after 1960.
#   - Store only the rows describing Avengers added in 1960 or later in true_avengers.
def main():
    avengers = pd.read_csv("avengers.csv")

    avengers['Year'].hist()
    plt.show()

    true_avengers = avengers[avengers['Year'] >= 1960].copy()

    true_avengers['Year'].hist()
    plt.show()


if __name__ == '__main__':
    main()
