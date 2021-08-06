import pandas as pd
import matplotlib.pyplot as plt


# - Generate a scatter plot with Slowness in traffic (%) on the x-axis and Point of flooding on the y-axis. Close and
#   display the plot using plt.show().
# - Generate a scatter plot with Slowness in traffic (%) on the x-axis and Semaphore off on the y-axis.
def main():
    traffic = pd.read_csv('../traffic_sao_paulo.csv', sep=';')
    #  Cleaning and converting 'Slowness in traffic (%)' column to  float dtype.
    traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.').astype(float)

    # Isolating the incident columns by dropping the columns 'Hour (Coded)' and 'Slowness in traffic (%)'
    incidents = traffic.drop(['Hour (Coded)', 'Slowness in traffic (%)'], axis=1)

    traffic.plot.scatter(x='Slowness in traffic (%)', y='Lack of electricity')
    plt.show()
    traffic.plot.scatter(x='Slowness in traffic (%)', y='Point of flooding')
    plt.show()
    traffic.plot.scatter(x='Slowness in traffic (%)', y='Semaphore off')
    plt.show()


if __name__ == '__main__':
    main()
