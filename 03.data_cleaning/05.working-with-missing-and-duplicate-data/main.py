import pandas as pd


# - Use the DataFrame.shape attribute to confirm the number of rows and columns for happiness2015, happiness2016, and
#   happiness2017.
#   - Assign the result for happiness2015 to shape_2015.
#   - Assign the result for happiness2016 to shape_2016.
#   - Assign the result for happiness2017 to shape_2017.
def main():
    happiness2015 = pd.read_csv('wh_2015.csv')
    happiness2016 = pd.read_csv('wh_2016.csv')
    happiness2017 = pd.read_csv('wh_2017.csv')

    shape_2015 = happiness2015.shape
    shape_2016 = happiness2016.shape
    shape_2017 = happiness2017.shape

    print(shape_2015, shape_2016, shape_2017, sep='\n')


if __name__ == '__main__':
    main()
