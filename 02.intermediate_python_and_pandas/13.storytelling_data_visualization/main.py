import pandas as pd
import matplotlib.pyplot as plt


# - Iterate over a list containing the four Axes objects. For each Axes object, do the following:
# - Generate a line plot with the Month column on the x-axis and the New_deaths columns on the y-axis.
# - Remove the x- and y-tick labels.
# - Remove all ticks using the Axes.tick_params() method.
# - Remove all the spines using the Axes.spines[location].set_visible() method.
def main():
    death_toll = pd.read_csv('../covid_avg_deaths.csv')
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, figsize=(6, 8))

    for ax in [ax1, ax2, ax3, ax4]:
        ax.plot(death_toll['Month'], death_toll['New_deaths'])

        # Maximizing data-ink ratio
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        ax.tick_params(left=False, bottom=False)

        for location in ['left', 'bottom', 'right', 'top']:
            ax.spines[location].set_visible(False)
        # =========================
    plt.show()


if __name__ == '__main__':
    main()
