import pandas as pd
import matplotlib.pyplot as plt


# - Create a new figure with figsize=(10,12).
# - Create the first five plots using a for loop. Iterate over both a range (use the range() function) and the days
#   list. For each iteration, do the following:
#   - Add the proper index number inside plt.subplot(nrows, ncols, index).
#   - Generate a line plot for each day — Hour (Coded) must be on the x-axis and Slowness in traffic (%) on the y-axis.
#   - Add the day name as a plot title.
#   - Bring the plot to a 0-25 range on the y-axis.
def main():
    traffic = pd.read_csv('../traffic_sao_paulo.csv', sep=';')
    #  Cleaning and converting 'Slowness in traffic (%)' column to  float dtype.
    traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.').astype(float)

    # Isolating the data for each day — from Monday to Friday
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    traffic_per_day = {}

    for i, day in zip(range(0, 135, 27), days):
        each_day_traffic = traffic[i:i + 27]
        traffic_per_day[day] = each_day_traffic

    plt.figure(figsize=(10, 12))
    for i, day in zip(range(1, 6), days):
        plt.subplot(3, 2, i)
        df = traffic_per_day[day]
        plt.plot(df['Hour (Coded)'], df['Slowness in traffic (%)'])
        plt.title(day)
        plt.ylim([0, 25])
    plt.show()


if __name__ == '__main__':
    main()
