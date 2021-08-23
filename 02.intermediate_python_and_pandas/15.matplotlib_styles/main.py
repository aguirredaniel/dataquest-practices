import pandas as pd
import matplotlib.pyplot as plt


# - Read in the winequality-white.csv file into a pandas DataFrame.
#   - Use sep=';' to properly read the file.
#   - Assign the result to white_wine.
# - Calculate the correlation between quality and the other columns of white_wine.
#   - The result should be a pandas Series with the same structure as the Series resulted from
#     red_wine.corr()['quality'][:-1].
#   - Assign the correlation values to white_corr.
# - Examine the correlation values — what are the strongest two correlations? How does this compare to the red wine
#   values?
def main():
    red_wine = pd.read_csv('winequality-red.csv', sep=';')
    red_corr = red_wine.corr()['quality'][:-1]

    white_wine = pd.read_csv('winequality-white.csv', sep=';')
    white_corr = white_wine.corr()['quality'][:-1]
    print(red_corr, white_corr, sep='\n\n')


if __name__ == '__main__':
    main()
