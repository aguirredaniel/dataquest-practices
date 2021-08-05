import pandas as pd
import matplotlib.pyplot as plt


# - The correlation between temp and cnt is +0.63, so it's stronger than the correlation between windspeed and cnt,
#   which is -0.23 (the two correlation values are real). Assign the Boolean True or False to sentence_1.
# - A correlation of +0.09 shows a weak positive correlation. Assign True or False to sentence_2.
# - A correlation of 0 shows a very weak negative correlation. Assign True or False to sentence_3.
# - A perfect positive correlation is equal in strength with a perfect negative correlation. Assign True or False to
#   sentence_4.
def main():
    bike_sharing = pd.read_csv('../day.csv')
    bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

    sentence_1 = True
    sentence_2 = True
    sentence_3 = False
    sentence_4 = True


if __name__ == '__main__':
    main()
