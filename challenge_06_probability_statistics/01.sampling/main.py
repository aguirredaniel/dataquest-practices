import pandas as pd
import matplotlib.pyplot as plt


# - Pick four team clusters randomly using the technique we've learned (use random_state = 0).
# - Collect the data from each cluster without sampling the clusters. Create a new DataFrame object that stores the data
#   collected from all clusters.
# - Use the data collected to estimate the mean for the following player attributes:
#   - Height
#   - Age
#   - BMI
#   - Total points
# - Finally, measure the sampling error of your estimates, and assign the errors to the following variables:
#   sampling_error_height, sampling_error_age, sampling_error_BMI, sampling_error_points.

def main():
    wnba = pd.read_csv('wnba.csv')

    teams = pd.Series(wnba['Team'].unique()).sample(4, random_state=0)
    clusters = [wnba[wnba['Team'] == team] for team in teams]
    sample = pd.concat(clusters)

    columns = ['Height', 'Age', 'BMI', 'PTS']
    statistics = sample[columns].mean()
    parameters = wnba[columns].mean()
    sampling_error_height, sampling_error_age, sampling_error_BMI, sampling_error_points = parameters - statistics

    print(sampling_error_height, sampling_error_age, sampling_error_BMI, sampling_error_points, sep='\n')


if __name__ == '__main__':
    main()
