import pandas as pd


# While the FiveThirtyEight team did a wonderful job acquiring the data, it still has some inconsistencies. Your lesson,
# if you choose to accept it, is to clean up their dataset so it can be more useful for analysis in pandas. Let's read
# it into pandas as a dataframe and preview the first five rows to get a better sense of it.
def main():
    avengers = pd.read_csv("avengers.csv")
    print(avengers.head(5))


if __name__ == '__main__':
    main()
