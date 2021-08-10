import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# - Add the Year column by building two different plots based on the values in this column.
# - Evaluate the truth value of the following sentences:
#   - Most houses built in 2000 or later have a living area aboveground between 1,000 and 3,000 square feet and sell for
#     more than 100,000 USD. Assign True or False to sentence_1.
#   - Most of the houses with an overall quality rating of four or less were built in 1999 or earlier, have low garage
#     area and six rooms or less. Assign True or False to sentence_2.
def main():
    housing = pd.read_csv('../housing.csv')

    sns.set_theme()
    sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice',
                hue='Overall Qual', palette='RdYlGn',
                size='Garage Area', sizes=(1, 300),
                style='Rooms', col='Year')
    plt.show()

    sentence_1 = True
    sentence_2 = True


if __name__ == '__main__':
    main()
