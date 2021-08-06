import pandas as pd
import matplotlib.pyplot as plt


# - Isolate all the rows where traffic slowness is 20% or more. Assign the new DataFrame to a variable named
#   slowness_20_or_more.
# - Drop the Slowness in traffic (%) and Hour (Coded) columns from slowness_20_or_more.
# - Calculate the event frequencies using the DataFrame.sum() method on slowness_20_or_more. Assign the resulting Series
#   to incident_frequencies.
# - Use incident_frequencies to plot a horizontal bar plot — use a Pandas method.
# - Examine the plot — what are some high-frequency incidents when traffic slowness is 20% or more?
def main():
    traffic = pd.read_csv('../traffic_sao_paulo.csv', sep=';')
    #  Cleaning and converting 'Slowness in traffic (%)' column to  float dtype.
    traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.').astype(float)

    slowness_20_or_more = traffic[traffic['Slowness in traffic (%)'] >= 20]
    slowness_20_or_more = slowness_20_or_more.drop(['Hour (Coded)', 'Slowness in traffic (%)'], axis=1)
    incident_frequencies = slowness_20_or_more.sum()
    print(incident_frequencies)

    incident_frequencies.plot.barh()
    plt.show()


if __name__ == '__main__':
    main()
