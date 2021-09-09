import pandas as pd


# - Use the df.groupby() method to group happiness2015 by the Region column. Assign the result to grouped.
# - Use the GroupBy.get_group() method to select the data for the Australia and New Zealand group only. Assign the
#   result to aus_nz.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    grouped = happiness2015.groupby('Region')
    aus_nz = grouped.get_group('Australia and New Zealand')
    print(aus_nz)


if __name__ == '__main__':
    main()
