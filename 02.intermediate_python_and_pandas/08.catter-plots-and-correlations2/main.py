import pandas as pd
import matplotlib.pyplot as plt


# - Generate a scatter plot with the atemp column (feeling temperature) on the x-axis and the registered column on the
#   y-axis.
# - Run your code without submitting the answer. Inspect the resulting scatter plot.
# - What type of correlation do you see between the atemp and registered columns? Assign your answer to the variable
#   correlation — choose between the strings 'positive', 'negative', and 'no correlation'.
def main():
    bike_sharing = pd.read_csv('../day.csv')
    bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

    plt.scatter(bike_sharing['atemp'], bike_sharing['registered'])
    plt.show()
    correlation = 'positive'


if __name__ == '__main__':
    main()
