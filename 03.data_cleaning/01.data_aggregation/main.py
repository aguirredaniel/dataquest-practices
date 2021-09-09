import numpy as np
import pandas as pd


def dif(group):
    return (group.max() - group.mean())


# - Inspect the following code: happiness_means = happiness2015.groupby('Region')['Happiness Score'].mean(). Try to
#   answer the questions below before running the code and moving on. There is no answer-checking on this screen.
# - If we run the code above, will the index of happiness_means be the unique values in the Region column or the
#   Happiness Score column?
# - Will the values aggregated in happiness_means be the values from the Region column or the Happiness Score column?
# - Print happiness_means. Were your predictions correct?
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    happiness_means = happiness2015.groupby('Region')['Happiness Score'].mean()
    print(happiness_means)


if __name__ == '__main__':
    main()
