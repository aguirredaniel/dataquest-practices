import pandas as pd


# - Import the pandas module as pd.
# - Read in the traffic_sao_paulo.csv file using pd.read_csv().
#   - The data points are separated by ;, so you'll need to use sep=';' to read in the file properly.
#   - Assign the result to a variable named traffic.
# - Perform a quick examination of the dataset.
#   - Inspect the first and the last five rows.
#   - Use DataFrame.info() to print summary information about the dataset. Do you see any missing values? Are all data
#     types numerical?
def main():
    traffic = pd.read_csv('../traffic_sao_paulo.csv', sep=';')
    print(traffic.head(), traffic.tail(), traffic.info(), sep='\n')


if __name__ == '__main__':
    main()
