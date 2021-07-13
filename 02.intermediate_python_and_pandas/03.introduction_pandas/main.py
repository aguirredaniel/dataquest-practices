import pandas as pd


# 1. Use the head() method to select the first 6 rows. Assign the result to f500_head.
# 2. Use the tail() method to select the last 8 rows. Assign the result to f500_tail.
def main():
    f500 = pd.read_csv('../f500.csv', index_col=1)
    f500_head = f500.head(6)
    f500_tail = f500.tail(8)
    print(f500_head, f500_tail, sep='\n')


if __name__ == "__main__":
    main()
