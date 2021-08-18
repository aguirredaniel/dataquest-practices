import pandas as pd
import matplotlib.pyplot as plt


# - Remove all four spines from the horizontal bar plot.
# - Remove the bottom and left ticks from the horizontal bar plot.
def main():
    top20_deathtoll = pd.read_csv('../top20_deathtoll.csv')
    figure, axes = plt.subplots(figsize=(4.5, 6))
    axes.barh(top20_deathtoll['Country_Other'], top20_deathtoll['Total_Deaths'])

    for spin in ['left', 'bottom', 'right', 'top']:
        axes.spines[spin].set_visible(False)

    axes.tick_params(bottom=False, left=False)
    plt.show()


if __name__ == '__main__':
    main()
