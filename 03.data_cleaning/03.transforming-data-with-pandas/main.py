import pandas as pd


def label(factor):
    """
    Indicate whether the factor has a high impact on the happiness score or a low impact
    Args:
        factor:

    Returns:
        str: A label for impact of factor. Two possible values can be returned: High or Low

    Examples:
        >>> label(1.39651)
        'High'

        >>> label(0.90563)
        'Low'
    """
    if factor > 1:
        return 'High'
    else:
        return 'Low'


def v_counts(col: pd.Series) -> pd.Series:
    """
    Calculates the percentage of 'High' and 'Low' values in factor series.
    Args:
        col:
        pd.Series for a Factor column with values 'High' and 'Low' impact.
    Returns:
        Returns a pd.Series with percentage of 'High' and 'Low' values.
    Examples:
        >>> series = pd.Series(['High', 'Low', 'Low'])
        >>> series
            0    High
            1    Low
            2    Low
        >>> v_counts(series)
            Low     0.666667
            High    0.333333
    """
    num = col.value_counts()
    den = col.size
    result = num / den

    return result


class Percentages:
    def __init__(self, df):
        self._df = df

    def __call__(self, col: pd.Series) -> pd.Series:
        """
            Converts a factor column to percentages of 'Happiness Score' column.
        Args:
            col:

        Returns:
            A pd.Series with the percentages of 'Happiness Score' column represent a Factor column.
        """
        div = col / self._df['Happiness Score']
        return div * 100


# - Use the melt function to reshape happiness2015. The columns listed in main_cols should stay the same. The columns
#   listed in factors should be transformed into rows. Assign the result to a variable called melt.
# - Convert the value column to a percentage.
#   - Divide the value column by the Happiness Score column and multiply the result by 100.
#   - Use the round() function to round the result to 2 decimal places.
#   - Assign the result to a new column called Percentage.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    mapping = {'Economy (GDP per Capita)': 'Economy', 'Health (Life Expectancy)': 'Health',
               'Trust (Government Corruption)': 'Trust'}

    #  DataFrame with factor columns renamed.
    happiness2015 = happiness2015.rename(mapping, axis=1)

    main_cols = ['Country', 'Region', 'Happiness Rank', 'Happiness Score']
    factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity', 'Dystopia Residual']

    melt = pd.melt(happiness2015, id_vars=main_cols, value_vars=factors)

    percentage = (melt['value'] / melt['Happiness Score']) * 100
    melt['Percentage'] = round(percentage, 2)


if __name__ == '__main__':
    main()
