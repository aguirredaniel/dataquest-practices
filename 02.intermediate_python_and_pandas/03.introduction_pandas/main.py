import pandas as pd


# 1. Use Python's type() function to assign the type of f500 to f500_type.
# 2. Use the DataFrame.shape attribute to assign the shape of f500 to f500_shape.
def main():
    f500 = pd.read_csv('../f500.csv', index_col=1)
    f500_type = type(f500)
    f500_shape = f500.shape

    print(f500_type, f500_shape, sep='\n')


if __name__ == "__main__":
    main()
