import pandas as pd
import matplotlib.pyplot as plt


# - Add the label Mar - Jun to the second Axes object. The label must have the following properties:
#   - The x-coordinate is 3.7.
#   - The y-coordinate is 800.
#   - The color is #af0b1e.
#   - It is bolded.
# - Add the label Jun - Oct to the third Axes object. The label must have the following properties:
#   - The x-coordinate is 7.1.
#   - The y-coordinate is 500.
#   - The color is #af0b1e.
#   - It is bolded.
# - Add the label Oct - Dec to the fourth Axes object. The label must have the following properties:
#   - The x-coordinate is 10.5.
#   - The y-coordinate is 600.
#   - The color is #af0b1e.
#   - It is bolded.
#   - It is rotated to 45 degrees.
def main():
    death_toll = pd.read_csv('../covid_avg_deaths.csv')
    fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(6, 8))
    periods = [(0, 3), (2, 6), (5, 10), (9, 12)]
    periods_labels_params = [(1.1, -300, 'Jan - Mar', 3),
                             (3.7, 800, 'Mar - Jun', 0),
                             (7.1, 500, 'Jun - Oct', 0),
                             (10.5, 600, 'Oct - Dec', 45)]

    # [y-axis] Showing  magnitude and the range of the quantities trends.
    ax1 = axes[0]
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
