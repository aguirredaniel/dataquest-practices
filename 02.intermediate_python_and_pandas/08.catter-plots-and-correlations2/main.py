import pandas as pd
import matplotlib.pyplot as plt


# - The worse the weather, the higher the encoding number in the weathersit column. Assign True or False to sentence_1.
# - The correlation between weathersit and cnt is -0.30 — this means that as the weather gets worse, the number of bike
#   rentals tends to decrease. Assign True or False to sentence_2.
# - The correlation between weathersit and hum is +0.59 — this means that as the humidity decreases, the weather tends
#   to get better. Assign True or False to sentence_3.
def main():
    bike_sharing = pd.read_csv('../day.csv')
    bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

    sentence_1 = True
    sentence_2 = True
    sentence_3 = False


if __name__ == '__main__':
    main()
