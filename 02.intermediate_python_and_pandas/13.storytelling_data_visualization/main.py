import pandas as pd
import matplotlib.pyplot as plt


# - Read in the covid_avg_deaths.csv file into a pandas DataFrame, and assign the result to a variable named death_toll.
# - Create a grid chart of four rows by one column with a figure size of (6, 8).
# - On each of the four plots, draw a line plot with the Month column on the x-axis and the New_deaths columns on the
#   y-axis.
def main():
    death_toll = pd.read_csv('../covid_avg_deaths.csv')
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, figsize=(6, 8))
    for ax in [ax1, ax2, ax3, ax4]:
        ax.plot(death_toll['Month'], death_toll['New_deaths'])
    plt.show()


if __name__ == '__main__':
    main()
