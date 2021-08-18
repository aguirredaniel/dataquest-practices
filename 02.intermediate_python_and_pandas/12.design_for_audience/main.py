import pandas as pd
import matplotlib.pyplot as plt


# - Change the x-tick labels to 0, 150,000, and 300,000.
# - Left-align all y-tick labels. Each label must have the coordinates x=-80000 and y=i-0.15, where i is an integer in
#   the range(0, 21).
# - Add a vertical line with the following properties:
#  - Its x-coordinate is 150000
#  - Its ymin is 0.045
#  - It has a gray color
# - It has a transparency of 0.5
def main():
    top20_deathtoll = pd.read_csv('../top20_deathtoll.csv')
    figure, axes = plt.subplots(figsize=(4.5, 6))
    axes.barh(top20_deathtoll['Country_Other'], top20_deathtoll['Total_Deaths'],
              height=0.45, color='#af0b1e')

    for spin in ['left', 'bottom', 'right', 'top']:
        axes.spines[spin].set_visible(False)

    axes.set_xticks([0, 150000, 300000])
    axes.set_xticklabels(['0', '150,000', '300,000'])

    axes.set_yticklabels([])

    for i, country in zip(range(0, 21), top20_deathtoll['Country_Other']):
        axes.text(x=-80000, y=i - 0.15, s=country)

    axes.xaxis.tick_top()
    axes.tick_params(axis='x', colors='grey')
    axes.tick_params(top=False, left=False)

    axes.text(x=-80000, y=23.5, s='The Death Toll Worldwide Is 1.5M+', size=17, weight='bold')
    axes.text(x=-80000, y=22.5, s='Top 20 countries by death toll (December 2020)', size=12)

    axes.axvline(x=150000, ymin=0.045, c='grey', alpha=0.5)
    plt.show()


if __name__ == '__main__':
    main()
