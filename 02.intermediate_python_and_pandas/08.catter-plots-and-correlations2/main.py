import pandas as pd
import matplotlib.pyplot as plt


# - Plot a line graph with the dteday column on the x-axis and the temp column on the y-axis.
# - Rotate the x-ticks to an angle of 45 degrees using plt.xticks().
# - Do you see any similarity in how the temperature and the number of bikes rented change?
def main():
    bike_sharing = pd.read_csv('../day.csv')
    bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

    plt.plot(bike_sharing['dteday'], bike_sharing['temp'])
    plt.xticks(rotation=45)
    plt.show()


if __name__ == '__main__':
    main()
