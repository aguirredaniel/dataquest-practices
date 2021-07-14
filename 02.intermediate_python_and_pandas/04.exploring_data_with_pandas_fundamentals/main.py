import pandas as pd


# 1. Use the DataFrame.max() method to find the maximum value for only the numeric columns from f500
#    (you may need to check the documentation). Assign the result to the variable max_f500.
def main():
    f500 = pd.read_csv('../f500.csv')
    max_f500 = f500.max(numeric_only=True)

    print(max_f500, sep='\n')


if __name__ == "__main__":
    main()
