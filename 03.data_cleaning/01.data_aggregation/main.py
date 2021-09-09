import pandas as pd


# - Use the pd.read_csv() function to read the World_Happiness_2015.csv file into a DataFrame called happiness2015.
# - Store the first five rows of the DataFrame in a variable called first_5.
# - Use the DataFrame.info() method to print information about the DataFrame.
# - After you run your code, use the variable inspector to look at the variable first_5 and the output to become
#   familiar with the data.

def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    first_5 = happiness2015.head()
    print(happiness2015.info(), first_5, sep='\n')


if __name__ == '__main__':
    main()
