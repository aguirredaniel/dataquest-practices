import pandas as pd
import matplotlib.pyplot as plt


# -Reduce the thickness of each bar to a value of 0.45.
# - Keep only 0, 150000, and 300000 as x-tick labels.
def main():
    top20_deathtoll = pd.read_csv('../top20_deathtoll.csv')
    figure, axes = plt.subplots(figsize=(4.5, 6))
    axes.barh(top20_deathtoll['Country_Other'], top20_deathtoll['Total_Deaths'],
              height=0.45)

    for spin in ['left', 'bottom', 'right', 'top']:
        axes.spines[spin].set_visible(False)

    axes.tick_params(bottom=False, left=False)

    axes.set_xticks([0, 150000, 300000])

    plt.show()


if __name__ == '__main__':
    main()
