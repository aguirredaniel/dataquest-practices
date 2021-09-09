import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def dif(group):
    return (group.max() - group.mean())


# - Plot the resulting DataFrame, pv_happiness, using the df.plot() method. Set kind to barh, xlim to (0,10), title to
#   'Mean Happiness Scores by Region', and legend to False. What do you notice about these results?
# - Calculate the mean of the Happiness Score column in the original happiness 2015 data set. Assign the result to
#   world_mean_happiness.
#   - Does world_mean_happiness equal the value for the All group? If you can't figure out the answer, don't worry!
#     We'll review this question on the next screen.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    pv_happiness = happiness2015.pivot_table(values='Happiness Score', index='Region', aggfunc=np.mean, margins=True)
    pv_happiness.plot(kind='barh', xlim=(0, 10), title='Mean Happiness Scores by Region')
    plt.show()

    world_mean_happiness = happiness2015['Happiness Score'].mean()
    print(world_mean_happiness)


if __name__ == '__main__':
    main()
