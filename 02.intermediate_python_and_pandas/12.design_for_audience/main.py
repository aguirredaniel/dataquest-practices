import pandas as pd
import matplotlib.pyplot as plt


# - Recreate the horizontal bar plot with a width of 4.5 inches and a height of 6 inches.
def main():
    top20_deathtoll = pd.read_csv('../top20_deathtoll.csv')
    figure, axes = plt.subplots(figsize=(4.5, 6))
    axes.barh(top20_deathtoll['Country_Other'], top20_deathtoll['Total_Deaths'])
    plt.show()


if __name__ == '__main__':
    main()
