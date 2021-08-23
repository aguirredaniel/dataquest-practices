import pandas as pd
import matplotlib.pyplot as plt


# - Using the Axes.axvline() method:
# - Add a vertical line to the left of the labels column. The line should have the following properties:
#   - The x-coordinate is 0.5.
#  -  The color is grey.
#  -  The alpha value is 0.1.
#  -  The line width is 1.
#   - The ymin is 0.1 and the ymax is 0.9.
# - Add a vertical line to the right of the labels column. The line should have the following properties:
#   - The x-coordinate is 1.45.
#   - The color is grey.
#   - The alpha value is 0.1.
#   - The line width is 1.
#   - The ymin is 0.1 and the ymax is 0.9.
def main():
    red_wine = pd.read_csv('winequality-red.csv', sep=';')
    red_corr = red_wine.corr()['quality'][:-1]

    white_wine = pd.read_csv('winequality-white.csv', sep=';')
    white_corr = white_wine.corr()['quality'][:-1]

    plt.style.use('fivethirtyeight')
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.barh(white_wine.columns[:-1], white_corr, left=2,
            height=0.5)
    ax.barh(red_wine.columns[:-1], red_corr, left=-0.1,
            height=0.5)

    ax.grid(False)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    x_coords = {'Alcohol': 0.82, 'Sulphates': 0.77, 'pH': 0.91,
                'Density': 0.80, 'Total Sulfur Dioxide': 0.59,
                'Free Sulfur Dioxide': 0.6, 'Chlorides': 0.77,
                'Residual Sugar': 0.67, 'Citric Acid': 0.76,
                'Volatile Acidity': 0.67, 'Fixed Acidity': 0.71}
    y_coord = 9.8

    for y_label, x_coord in x_coords.items():
        ax.text(x_coord, y_coord, y_label)
        y_coord -= 1

    ax.axvline(x=0.5, color='grey', alpha=0.1,
             linewidth=1, ymin=0.1, ymax=0.9)

    ax.axvline(x=1.45, color='grey', alpha=0.1,
             linewidth=1, ymin=0.1, ymax=0.9)

    plt.show()


if __name__ == '__main__':
    main()
