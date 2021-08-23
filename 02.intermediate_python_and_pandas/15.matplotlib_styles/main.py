import pandas as pd
import matplotlib.pyplot as plt


# - Create a pandas Series for the red wine data set to specify the color order.
#   - The correlation values are already saved in red_corr.
#   - Zero and positive correlation values should have the color code '#33A1C9'.
#   - Negative correlation values should have the color code '#ffae42'.
# - Use the Series you've just created to change the colors of the bars in the red wine bar plot.
def main():
    red_wine = pd.read_csv('winequality-red.csv', sep=';')
    red_corr = red_wine.corr()['quality'][:-1]

    white_wine = pd.read_csv('winequality-white.csv', sep=';')
    white_corr = white_wine.corr()['quality'][:-1]

    plt.style.use('fivethirtyeight')
    fig, ax = plt.subplots(figsize=(9, 5))

    white_positive = white_corr >= 0
    color_map_white = white_positive.map({True: '#33A1C9', False: '#ffae42'})

    red_positive = red_corr >= 0
    color_map_red = red_positive.map({True: '#33A1C9', False: '#ffae42'})

    ax.barh(white_wine.columns[:-1], white_corr, left=2,
            height=0.5, color=color_map_white)
    ax.barh(red_wine.columns[:-1], red_corr, left=-0.1,
            height=0.5, color=color_map_red)

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

    ax.axhline(-1, color='grey', linewidth=1, alpha=0.5,
               xmin=0.01, xmax=0.32)
    ax.text(-0.7, -1.7, '-0.5' + ' ' * 31 + '+0.5',
            color='grey', alpha=0.5)

    ax.axhline(-1, color='grey', linewidth=1, alpha=0.5,
               xmin=0.67, xmax=0.98)
    ax.text(1.43, -1.7, '-0.5' + ' ' * 31 + '+0.5',
            color='grey', alpha=0.5)

    ax.axhline(11, color='grey', linewidth=1,
               alpha=0.5, xmin=0.01, xmax=0.32)
    ax.text(-0.33, 11.2, 'RED WINE', fontweight='bold')

    ax.axhline(11, color='grey', linewidth=1,
               alpha=0.5, xmin=0.67, xmax=0.98)
    ax.text(1.75, 11.2, 'WHITE WINE', fontweight='bold')

    ax.text(-0.7, -2.9,
            '©DATAQUEST' + ' ' * 94 + 'Source: P. Cortez et al.',
            color='#f0f0f0', backgroundcolor='#4d4d4d',
            size=12)

    ax.text(-0.7, 13.5, 'Wine Quality Most Strongly Correlated With Alcohol Level',
            fontsize=15, fontweight='bold')
    ax.text(-0.7, 12.7,
            'Correlation values between wine quality and wine properties (alcohol, pH, etc.)')

    plt.show()

if __name__ == '__main__':
        main()
