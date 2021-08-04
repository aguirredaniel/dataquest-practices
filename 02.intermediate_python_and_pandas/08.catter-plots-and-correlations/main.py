import pandas as pd
import matplotlib.pyplot as plt


# - Generate a scatter plot with the workingday column on the x-axis and the casual column on the y-axis. Add
#   'Working Day Vs. Casual' as a title.
# - Generate a scatter plot with the workingday column on the x-axis and the registered column on the y-axis. Add
#   'Working Day Vs. Registered' as a title. You'll first need to close the previous scatter plot using plt.show()
# - Do you notice an opposing pattern between the two scatter plots? The scatter plots might look a bit odd at first,
#   but recall workingday only has two unique values, so you'll see two narrow vertical strips on the plots.
def main():
    bike_sharing = pd.read_csv('../day.csv')
    bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

    working_day = bike_sharing['workingday']
    casual = bike_sharing['casual']

    plt.scatter(working_day, casual)
    plt.title('Working Day Vs. Casual')
    plt.show()

    registered = bike_sharing['registered']
    plt.scatter(working_day, registered)
    plt.title('Working Day Vs. Registered')
    plt.show()


if __name__ == '__main__':
    main()
