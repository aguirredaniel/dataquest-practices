import pandas as pd
import matplotlib.pyplot as plt


# - Inside the code editor, we've already added three plots on the grid chart. Add the other three plots.
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

    plt.figure()
    for i in range(6):
        plt.subplot(3, 2, i + 1)
    plt.show()


if __name__ == '__main__':
    main()
