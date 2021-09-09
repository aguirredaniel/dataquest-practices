import pandas as pd


# - Select only the Happiness Score column from grouped. Assign the result to happy_grouped.
# - Use the GroupBy.mean() method to compute the mean of happy_grouped. Assign the result to happy_mean.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    grouped = happiness2015.groupby('Region')
    happy_grouped = grouped['Happiness Score']
    happy_mean = happy_grouped.mean()
    print(happy_mean)


if __name__ == '__main__':
    main()
