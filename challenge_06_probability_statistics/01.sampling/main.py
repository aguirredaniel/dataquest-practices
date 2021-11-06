import pandas as pd
import matplotlib.pyplot as plt


# 1. Minimize the variability within each stratum.
#    For instance, avoid having in the same stratum a player that has scored 10 points and a player that has scored 500.
#    If the variability is high, it might be a sign that you either need more granular stratification (you need more
#    strata), or you need to change the criterion of stratification (an example of criterion is minutes played).
# 2. Maximize the variability between strata.
#    Good strata are different from one another. If you have strata that are similar to one another with respect to what
#    you want to measure, you might need a more granular stratification, or you might need to change the stratification
#    criterion. On the previous screen, stratifying the data by games played resulted in strata that were similar to
#    each other regarding the distribution of the total points. We managed to increase the variability between strata
#    by changing the criterion of stratification to minutes played.
# 3. The stratification criterion should correlate strongly with the property you're trying to measure.
#    For instance, the column describing minutes played (the criterion) should be correlate strongly with the number of
#    total points (property we want to measure).

def main():
    wnba = pd.read_csv('wnba.csv')

    minutes_played = wnba['MIN']
    intervals = minutes_played.value_counts(bins=3, normalize=True)
    print(intervals)

    strata = [wnba[(minutes_played > interval.left) & (minutes_played <= interval.right)]['PTS']
              for interval in intervals.index]

    statistics = []
    for i in range(100):
        srs = [s.sample(n=3, random_state=i) for s in strata]
        sample = pd.concat(srs)
        statistic = sample.mean()
        statistics.append(statistic)

    parameter = wnba['PTS'].mean()
    plt.scatter(x=range(1, 101), y=statistics)
    plt.axhline(parameter)
    plt.show()


if __name__ == '__main__':
    main()
