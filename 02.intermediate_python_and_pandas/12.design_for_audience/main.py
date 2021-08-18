import pandas as pd
import matplotlib.pyplot as plt


# - Use the Axes.barh() method to recreate the horizontal bar plot we previously generated.
# - Call plt.show() to display the plot.
def main():
    top20_deathtoll = pd.read_csv('../top20_deathtoll.csv')
    figure, axes = plt.subplots()
    axes.barh(top20_deathtoll['Country_Other'], top20_deathtoll['Total_Deaths'])
    plt.show()


if __name__ == '__main__':
    main()
