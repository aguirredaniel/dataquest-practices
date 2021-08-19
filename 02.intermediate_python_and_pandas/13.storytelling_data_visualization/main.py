import pandas as pd
import matplotlib.pyplot as plt


# - Add the title The virus kills 851 people each day to the first Axes object (data source: World Health Organization).
#   The text must have the following properties:
#   - The x-coordinate is 0.5.
#   - The y-coordinate is 3500.
#   - The font size is 14.
#   - It is bolded.
# - Add the subtitle Average number of daily deaths per month in the US. The text must have the following properties:
#   - The x-coordinate is 0.5.
#   - The y-coordinate is 3150.
#   - The font size is 12.
def main():
    death_toll = pd.read_csv('../covid_avg_deaths.csv')
    fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(6, 8))
    periods = [(0, 3), (2, 6), (5, 10), (9, 12)]
    periods_labels_params = [(1.1, -300, 'Jan - Mar', 3),
                             (3.7, 800, 'Mar - Jun', 0),
                             (7.1, 500, 'Jun - Oct', 0),
                             (10.5, 600, 'Oct - Dec', 45)]

    ax1 = axes[0]

    # [y-axis] Showing  title and sub-title.
    ax1.text(0.5, 3500, 'The virus kills 851 people each day', size=14, weight='bold')
    ax1.text(0.5, 3150, 'Average number of daily deaths per month in the US', size=12)

    # [y-axis] Showing  magnitude and the range of the quantities trends.
    ax1.text(0.5, -80, '0', alpha=0.5)
    ax1.text(3.5, 2000, '1,844', alpha=0.5)
    ax1.text(11.5, 2400, '2,247', alpha=0.5)

    for ax, period, period_label_params in zip(axes, periods, periods_labels_params):
        ax.plot(death_toll['Month'], death_toll['New_deaths'],
                color='#af0b1e', alpha=0.1)

        # Highlight periods
        start, finish = period
        ax.plot(death_toll['Month'][start: finish], death_toll['New_deaths'][start:finish],
                color='#af0b1e', linewidth=2.5)

        # Adding Progress bars
        ax.axhline(y=1600, xmin=0.5, xmax=0.8,
                   linewidth=6, color='#af0b1e', alpha=0.1)

        # [x-axis] Showing months periods labels
        x, y, label, rotation = period_label_params
        ax.text(x, y, label, color='#af0b1e',
                weight='bold', rotation=rotation)

        # Maximizing data-ink ratio
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        ax.tick_params(left=False, bottom=False)

        for location in ['left', 'bottom', 'right', 'top']:
            ax.spines[location].set_visible(False)

    plt.show()


if __name__ == '__main__':
    main()
