import pandas as pd
import matplotlib.pyplot as plt


# - Import matplotlib.pyplot, and plot a histogram for the Slowness in traffic (%) column — run your code without
#   submitting the answer.
# - Based on the histogram, evaluate the truth value of the sentences below.
#   - The distribution of Slowness in traffic (%) is right skewed. Assign the Boolean True or False to sentence_1.
#   - Most of the values pile up on the left side of the histogram. Assign True or False to sentence_2.
#   - Most of the values are over 15.0%. Assign True or False to sentence_3.
def main():
    traffic = pd.read_csv('../traffic_sao_paulo.csv', sep=';')
    #  Cleaning and converting Slowness in traffic (%)' column to  float dtype.
    traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.').astype(float)

    plt.hist(traffic['Slowness in traffic (%)'])
    plt.show()

    sentence_1 = True
    sentence_2 = False
    sentence_3 = True

if __name__ == '__main__':
    main()
