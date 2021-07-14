import pandas as pd


# 1. The company "Dow Chemical" has named a new CEO. Update the value where the row label is Dow Chemical and for the
#    ceo column to Jim Fitterling in the f500 dataframe.
def main():
    f500 = pd.read_csv('../f500.csv')
    f500.loc['Dow Chemical', 'ceo'] = 'Jim Fitterling'



if __name__ == "__main__":
    main()
