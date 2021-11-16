import pandas as pd


def main():
    pd.options.display.max_rows = 200
    pd.options.display.max_columns = 50

    wnba = pd.read_csv('../data/wnba.csv')
    print(wnba.shape)
    print(wnba)


if __name__ == '__main__':
    main()
