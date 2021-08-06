import pandas as pd
import matplotlib.pyplot as plt


# - Generate a horizontal bar plot for the incidents.sum() table. Run your code without submitting the answer.
# - Based on the resulting bar plot, evaluate the truth value of the following sentences:
#   - Broken trucks are the most frequent cause of slow traffic. Assign the Boolean True or False to sentence_1.
#   - Lack of electricity and flooding are less frequent than broken trucks. Assign True or False to sentence_2.
#   - The most frequent incident type is broken trucks. Assign True or False to sentence_3.
def main():
    traffic = pd.read_csv('../traffic_sao_paulo.csv', sep=';')
    #  Cleaning and converting 'Slowness in traffic (%)' column to  float dtype.
    traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.').astype(float)

    # Isolating the incident columns by dropping the columns 'Hour (Coded)' and 'Slowness in traffic (%)'
    incidents = traffic.drop(['Hour (Coded)', 'Slowness in traffic (%)'], axis=1)

    incidents.sum().plot.barh()
    plt.show()

    sentence_1 = False
    sentence_2 = True
    sentence_3 = True


if __name__ == '__main__':
    main()
