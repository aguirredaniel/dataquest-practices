import pandas as pd
import matplotlib.pyplot as plt


# - Calculate the Pearson's r between the temp and atemp columns. Assign your answer to temp_atemp_corr.
# - Calculate the Pearson's r between the windspeed and hum columns. Assign your answer to wind_hum_corr.
# - Generate a scatter plot with the temp column on the x-axis and the atemp column on the y-axis.
#   - Add 'Air Temperature' as an x-label.
#   - Add 'Feeling Temperature' as an y-label.
# - Generate a scatter plot with the windspeed column on the x-axis and the hum column on the y-axis. You'll first need
#   to close the previous scatter plot using plt.show()
#   - Add 'Wind Speed' as an x-label.
#   - Add 'Humidity' as an y-label.
def main():
    bike_sharing = pd.read_csv('../day.csv')
    bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

    temp_atemp_corr = bike_sharing['temp'].corr(bike_sharing['atemp'])
    wind_hum_corr = bike_sharing['windspeed'].corr(bike_sharing['hum'])
    print(temp_atemp_corr, wind_hum_corr, sep='\n')

    plt.scatter(bike_sharing['temp'], bike_sharing['atemp'])
    plt.xlabel('Air Temperature')
    plt.ylabel('Feeling Temperature')
    plt.show()

    plt.scatter(bike_sharing['windspeed'], bike_sharing['hum'])
    plt.xlabel('Wind Speed')
    plt.ylabel('Humidity')
    plt.show()


if __name__ == '__main__':
    main()
