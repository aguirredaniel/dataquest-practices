import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def dif(group):
    return (group.max() - group.mean())


# - Use the df.groupby() method to calculate the minimum, maximum, and mean family and happiness scores for each region
#   in happiness2015.
#   - Group happiness2015 by the Region column.
#   - Select the Happiness Score and Family columns. Assign the result to grouped.
#   - Apply the GroupBy.agg() method to grouped. Pass a list containing np.min, np.max, and np.mean into the method.
#   - Assign the result to happy_family_stats.
# - Use the pivot_table method to return the same information, but also calculate the minimum, maximum, and mean for the
#   entire Family and Happiness Score columns.
#   - The aggregation columns should be Happiness Score and Family.
#   - The column to group by is Region.
#   - The aggregation functions are np.min, np.max, and np.mean.
#   - Set the margins parameter equal to True.
#   - Assign the result to pv_happy_family_stats.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    happy_family_stats = happiness2015.groupby('Region')[['Happiness Score', 'Family']].agg([np.min, np.max, np.mean])
    pv_happy_family_stats = happiness2015.pivot_table(
        values=['Family', 'Happiness Score'], index='Region', aggfunc=[np.min, np.max, np.mean], margins=True)

    print(happy_family_stats, pv_happy_family_stats, sep='\n')


if __name__ == '__main__':
    main()
