import numpy as np
import pandas as pd


def dif(group):
    return (group.max() - group.mean())


# - Apply the GroupBy.agg() method to happy_grouped. Pass a list containing np.mean and np.max into the method. Assign
#   the result to happy_mean_max.
# - As noted above, passing 'mean' and 'max' into the GroupBy.agg() method will also return the same results. However,
#   for answer-checking purposes, you'll have to use np.mean and np.max.
# - We've also created a custom function named dif to calculate the difference between the mean and maximum values. Pass
#   dif into the GroupBy.agg() method. Assign the result to mean_max_dif.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    grouped = happiness2015.groupby('Region')
    happy_grouped = grouped['Happiness Score']
    happy_mean_max = happy_grouped.agg([np.mean, np.max])
    mean_max_dif = happy_grouped.agg(dif)

    print(happy_mean_max, mean_max_dif, sep='\n')


if __name__ == '__main__':
    main()
