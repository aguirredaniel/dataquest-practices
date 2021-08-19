import pandas as pd
import matplotlib.pyplot as plt


# - Highlight the June–October period on the third plot. Use color='#af0b1e' and linewidth=2.5.
# - Highlight the October–December period on the fourth plot. Use color='#af0b1e' and linewidth=2.5.
def main():
    death_toll = pd.read_csv('../covid_avg_deaths.csv')
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(nrows=4, ncols=1, figsize=(6, 8))
    axes = [ax1, ax2, ax3, ax4]
    for ax in axes:
        ax.plot(death_toll['Month'], death_toll['New_deaths'],
                color='#af0b1e', alpha=0.1)

        # Maximizing data-ink ratio
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        ax.tick_params(left=False, bottom=False)

        for location in ['left', 'bottom', 'right', 'top']:
            ax.spines[location].set_visible(False)
        # =========================

    # Highlight periods
    for ax, periods in zip(axes, [(0, 3), (2, 6), (5, 10), (9, 12)]):
        start, finish = periods
        ax.plot(death_toll['Month'][start: finish], death_toll['New_deaths'][start:finish],
                color='#af0b1e', linewidth=3.5)

    plt.show()


if __name__ == '__main__':
    main()
