import pandas as pd
import matplotlib.pyplot as plt


# - Plot two line graphs sharing the same x- and y-axis.
#   - For the first graph, plot the dteday column on the x-axis and the casual column on the y-axis.
#   - For the second graph, plot dteday on the x-axis and registered on the y-axis.
# - Rotate the x-ticks to an angle of 30 degrees using plt.xticks().
# - Add the label 'Bikes Rented' to the y-axis using plt.ylabel().
# - Add the label 'Date' to the x-axis using plt.xlabel().
# - Add the title 'Bikes Rented: Casual vs. Registered' using plt.title().
# - Add a legend using plt.legend(). Use 'Casual' and 'Registered' as labels.
# - What differences and similarities do you see for the two line graphs?
def main():
    bike_sharing = pd.read_csv('../day.csv')
    bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

    plt.plot(bike_sharing['dteday'], bike_sharing['casual'])
    plt.plot(bike_sharing['dteday'], bike_sharing['registered'])

    plt.xticks(rotation=30)

    plt.ylabel('Bikes Rented')
    plt.xlabel('Date')
    plt.title('Bikes Rented: Casual vs. Registered')

    plt.legend(labels=['Casual', 'Registered'])

    plt.show()


if __name__ == '__main__':
    main()
