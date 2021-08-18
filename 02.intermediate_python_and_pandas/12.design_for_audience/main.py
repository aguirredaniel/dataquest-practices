import pandas as pd
import matplotlib.pyplot as plt


# Read in the top20_deathtoll.csv file into a pandas DataFrame. Assign the result to top20_deathtoll.
# Using matplotlib, create a horizontal bar plot to display the top 20 countries by number of total deaths.
def main():
    top20_deathtoll = pd.read_csv('top20_deathtoll.csv')
    plt.barh(top20_deathtoll['Country_Other'], top20_deathtoll['Total_Deaths'])
    plt.show()


if __name__ == '__main__':
    main()
