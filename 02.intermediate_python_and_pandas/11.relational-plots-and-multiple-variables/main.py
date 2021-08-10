import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# - Add the Garage Area variable on the graph by using a size representation. The size range should be between 1 and
#   300.
# - Evaluate the truth value of the following sentences:
#   - Houses that sell for more than 700,000 USD typically have garage areas greater than 1,000 square feet and living
#     areas aboveground lower than 4,000 square feet. Assign True or False to sentence_1.
#   - Houses with an overall quality of nine or ten typically have garage areas greater than 500 square feet, living
#     areas aboveground greater than 2,000 feet, and sell for more than 400,000 USD. Assign True or False to sentence_2
def main():
    housing = pd.read_csv('../housing.csv')

    sns.set_theme()
    sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice',
                hue='Overall Qual', palette='RdYlGn',
                size='Garage Area', sizes=(1, 300))
    plt.show()

    sentence_1 = False
    sentence_2 = True


if __name__ == '__main__':
    main()
