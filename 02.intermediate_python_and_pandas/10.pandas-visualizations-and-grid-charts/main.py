import pandas as pd
import matplotlib.pyplot as plt


# - Generate all the five line plots on a single graph. Use a for loop over the days list, and for each day, do the
#   following:
#   - Plot a line plot using plt.plot(): Hour (Coded) must be on the x-axis and Slowness in traffic (%) on the y-axis.
# - Add a legend to the graph.
#   - Outside the for loop, use plt.legend().
#   - Inside the for loop, use the label parameter inside plt.plot() — the label should be the day name.
def main():
    traffic = pd.read_csv('../traffic_sao_paulo.csv', sep=';')
    #  Cleaning and converting 'Slowness in traffic (%)' column to  float dtype.
    traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.').astype(float)

    # Isolating the data for each day — from Monday to Friday
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    traffic_per_day = {}

    for i, day in zip(range(0, 135, 27), days):
        print(i, i + 27)
        each_day_traffic = traffic[i:i + 27]
        traffic_per_day[day] = each_day_traffic

    for day in days:
        df = traffic_per_day[day]
        plt.plot(df['Hour (Coded)'], df['Slowness in traffic (%)'], label=day)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
