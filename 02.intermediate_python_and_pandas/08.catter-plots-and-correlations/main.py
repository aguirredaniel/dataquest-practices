import pandas as pd
import matplotlib.pyplot as plt


# - The distribution of the registered column looks similar to a normal distribution. Assign the Boolean True or False
#   to sentence_1.
# - Most days, registered users rent between 6,000 and 7,000 bikes. Assign True or False to sentence_2.
# - It's relatively rare that registered users rent fewer than 500 bikes in one day. Assign True or False to sentence_3.
# - The tallest bar on the histogram corresponds to a frequency of about 140 days. Assign True or False to sentence_4.
# - The histogram above has a total of 12 bars. Assign True or False to sentence_5.
def main():
    bike_sharing = pd.read_csv('../day.csv')
    bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

    plt.hist(bike_sharing['registered'])
    plt.show()

    sentence_1 = True
    sentence_2 = False
    sentence_3 = True
    sentence_4 = True
    sentence_5 = False


if __name__ == '__main__':
    main()
