import pandas as pd
import matplotlib.pyplot as plt


# - Generate a scatter plot with the windspeed column on the x-axis and the cnt column on the y-axis. Use the
#   plt.scatter() function.
# - Add the 'Wind Speed' x-axis label using plt.xlabel().
# - Add the 'Bikes Rented' y-axis label using plt.ylabel().
# - Display the plot using plt.show()
def main():
    bike_sharing = pd.read_csv('../day.csv')
    bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

    plt.scatter(bike_sharing['windspeed'], bike_sharing['cnt'])
    plt.xlabel('Wind Speed')
    plt.ylabel('Bikes Rented')
    plt.show()


if __name__ == '__main__':
    main()
