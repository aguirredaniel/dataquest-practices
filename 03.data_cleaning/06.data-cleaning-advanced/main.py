import pandas as pd


def main():
    hn = pd.read_csv('hacker_news.csv')
    print(hn.info(), hn.head(), sep='\n')


if __name__ == '__main__':
    main()
