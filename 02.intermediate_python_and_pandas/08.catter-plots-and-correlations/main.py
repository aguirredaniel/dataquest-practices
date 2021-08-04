import pandas as pd
import matplotlib.pyplot as plt


# - Generate a bar plot to display the weather patterns in 2012.
#   - Use the unique_values list for x-coordinates, and the weather_2012 list as bar heights.
#   - Use plt.xticks() to customize the x-ticks: the only tick labels displayed should be 1, 2, 3, and 4.
#   - Use 'Weather Patterns: 2012' as a title.
#   - Use 'Frequency' as an y-label.
#   - Use 'Unique Values' as an x-label.
#   - Close the bar plot using plt.show().
def main():
    bike_sharing = pd.read_csv('../day.csv')
    bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

    unique_values = [1, 2, 3, 4]
    weather_2012 = [237, 123, 6, 0]

    plt.bar(unique_values, weather_2012)
    plt.xticks(ticks=[1, 2, 3, 4])
    plt.title('Weather Patterns: 2012')
    plt.ylabel('Frequency')
    plt.xlabel('Unique Values')
    plt.show()


if __name__ == '__main__':
    main()
