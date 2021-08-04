import pandas as pd
import matplotlib.pyplot as plt


# - The casual distribution is not symmetrical. Assign the Boolean True or False to sentence_1.
# - Most days, casual users rent over 2,000 bikes. Assign True or False to sentence_2.
# - The cnt distribution is approximately symmetrical, and it looks more like a uniform distribution than a normal
#   distribution. Assign True or False to sentence_3.
# - The tallest bar on the cnt histogram corresponds to about 200 days. Assign True or False to sentence_4.
def main():
    bike_sharing = pd.read_csv('../day.csv')
    bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

    plt.hist(bike_sharing['cnt'])
    plt.show()

    plt.hist(bike_sharing['casual'])
    plt.show()

    sentence_1 = True
    sentence_2 = False
    sentence_3 = False
    sentence_4 = False


if __name__ == '__main__':
    main()
