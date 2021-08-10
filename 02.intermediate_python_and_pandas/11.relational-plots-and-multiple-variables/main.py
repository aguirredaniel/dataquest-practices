import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# - Add the Rooms column on the graph by using a shape representation. Leave the markers on default mode.
# - Evaluate the truth value of the following sentences:
#   - We can't find houses with seven rooms or more, and less than 2,000 square feet living area aboveground. Assign
#     True or False to sentence_1.
#   - Virtually all houses with seven rooms or more have an overall quality of seven or more. Assign True or False to
#     sentence_2.
def main():
    housing = pd.read_csv('../housing.csv')

    sns.set_theme()
    sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice',
                hue='Overall Qual', palette='RdYlGn',
                size='Garage Area', sizes=(1, 300),
                style='Rooms')
    plt.show()

    sentence_1 = False
    sentence_2 = False


if __name__ == '__main__':
    main()
