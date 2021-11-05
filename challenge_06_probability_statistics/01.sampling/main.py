import pandas as pd
import matplotlib.pyplot as plt


# Perform stratified sampling: stratify the dataset by player position, and then do simple random sampling on every
# stratum. At the end, use the sample to determine which position scores the highest number of points per game.
# - Create a new column that describes the number of points a player scored per game during the season. The number of
#   total points a player scored during the entire season is in the PTS column, and the number of games played is in the
#   Games Played column. Give the new column a relevant name.
# - Stratify the wnba data set by player position. The Pos column describes a player's position. Assign each stratum to
#   a different variable.
# - Loop through the strata, and for each stratum, do the following:
#    - Sample 10 observations using simple random sampling (set random_state = 0).
#    - Find the mean points per game using the sample. Use the new column you created earlier.
#    - Find a way to store the mean along with its corresponding position. You can use a dictionary.
# - Find the position that scores the highest number of points per game, and assign its name to a variable named
#   position_most_points.
# To find the dictionary key that has the greatest dictionary value, you can use this technique.
def main():
    wnba = pd.read_csv('wnba.csv')

    wnba['PTG'] = wnba['PTS'] / wnba['Games Played']

    strata = {pos: wnba[wnba['Pos'] == pos] for pos in wnba['Pos'].unique()}

    stratified_sampling = {pos: df['PTG'].sample(n=10, random_state=0).mean() for pos, df in strata.items()}
    position_most_points = max(stratified_sampling, key=stratified_sampling.get)

    print(position_most_points)


if __name__ == '__main__':
    main()
