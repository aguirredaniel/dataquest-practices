import pandas as pd
import matplotlib.pyplot as plt


# - Use the Series.plot.hist() method to generate a histogram for the Slowness in traffic (%) column.
# - Add the title Distribution of Slowness in traffic (%) (the answer checking is case-sensitive).
# - Add the x-label Slowness in traffic (%).
# - Display the plot using plt.show().
def main():
    traffic = pd.read_csv('../traffic_sao_paulo.csv', sep=';')
    #  Cleaning and converting 'Slowness in traffic (%)' column to  float dtype.
    traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.').astype(float)

    traffic['Slowness in traffic (%)'].plot.hist()
    plt.title('Distribution of Slowness in traffic (%)')
    plt.xlabel('Slowness in traffic (%)')
    plt.show()


if __name__ == '__main__':
    main()
