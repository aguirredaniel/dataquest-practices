import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# - Import seaborn and matplotlib using the standard aliases.
# - Set the visual properties to Seaborn defaults.
# - Using sns.relplot(), plot a scatter plot with Gr Liv Area on the x-axis and SalePrice on the y-axis.
# - Call plt.show() to display the plot. Run your code without submitting the answer.
# - Inspect the scatter plot and determine the correlation type. Assign your answer as a string to a variable named
#   correlation — the possible answers are 'negative', 'null', and 'positive'.
def main():
    housing = pd.read_csv('../housing.csv')
    print(housing.head(), housing.tail(), housing.info(), sep='\n')

    sns.set_theme()
    sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice')
    plt.show()

    correlation = 'positive'


if __name__ == '__main__':
    main()
