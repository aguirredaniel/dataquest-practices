import pandas as pd
import matplotlib.pyplot as plt


# Perform stratified sampling on the data set 100 times, and sample strata proportionally.
# - Stratify the dataset by the number of games played in the following way: the first stratum should include players
#   who played 12 games or fewer; the second stratum should players who played more than 12 games but up to 22
#   (included); the third stratum should include players who played more than 22 games (22 not included).
# - Perform stratified sampling 100 times. For each of the 100 iterations of a for loop, do the following:
#   - Sample each stratum proportionally. Sample at random: one sample observation from the first stratum, two sample
#      observations from the second, and seven sample observations from the third stratum (eventually, we'll concatenate
#      these sample observations and calculate the mean of the PTS column).
#   - random_state should vary from 0 to 99: 0 for the first iteration, 99 for the final iteration.
#   - Once you're done with the sampling for the current iteration of the loop, concatenate all the sample observations
#     into one final sample. You can use pd.concat().
#   - Compute the mean of the final sample, and append it to a list defined outside the loop. The mean should be for the
#     PTS column.
# - Display the entire sampling process.
#   - Using plt.scatter(), display the sampling means on a scatter plot. Place the means on the y-axis and the sample
#     numbers on the x-axis (the numbers should range from 1 to 100 - both endpoints included).
#   - Using plt.axhline(), display the population mean for the total points in the form of a horizontal line.
def main():
    wnba = pd.read_csv('wnba.csv')

    stratum1 = wnba[wnba['Games Played'] < 13]
    stratum2 = wnba[(wnba['Games Played'] >= 13) & (wnba['Games Played'] <= 22)]
    stratum3 = wnba[wnba['Games Played'] > 22]

    samples = []
    for i in range(100):
        srs_1 = stratum1['PTS'].sample(n=1, random_state=i)
        srs_2 = stratum2['PTS'].sample(n=2, random_state=i)
        srs_3 = stratum3['PTS'].sample(n=7, random_state=i)

        sample = pd.concat([srs_1, srs_2, srs_3])
        samples.append(sample.mean())

    parameter = wnba['PTS'].mean()

    plt.scatter(x=range(1, 101), y=samples)
    plt.axhline(parameter)
    plt.show()


if __name__ == '__main__':
    main()
