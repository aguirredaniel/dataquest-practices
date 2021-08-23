import pandas as pd
import matplotlib.pyplot as plt


# - Remove the grid of the graph using the Axes.grid() method. Read the documentation to find the parameter you need to
#   use.
# - Remove the x- and y-tick labels. Use the Axes.set_xticklabels() method and the Axes.set_yticklabels() method.
# - Reduce the width of each bar to 0.5 by using the Axes.barh() method — you'll need to use the height parameter.
def main():
    red_wine = pd.read_csv('winequality-red.csv', sep=';')
    red_corr = red_wine.corr()['quality'][:-1]

    white_wine = pd.read_csv('winequality-white.csv', sep=';')
    white_corr = white_wine.corr()['quality'][:-1]

    plt.style.use('fivethirtyeight')
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.barh(white_wine.columns[:-1], white_corr, left=2,
            height=0.5)
    ax.barh(red_wine.columns[:-1], red_corr,
            height=0.5)

    ax.grid(False)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    plt.show()


if __name__ == '__main__':
    main()
