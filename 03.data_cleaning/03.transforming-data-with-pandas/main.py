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


# - Create a function that converts each of the six factor columns and the Dystopia Residual column to percentages.
#   - Create a function named percentages that accepts one parameter called col.
#   - Divide col by the Happiness Score column. Assign the result to div.
#   - Multiply div by 100 and return the result.
# - Use the df.apply() method to apply the percentages function to all of the columns in factors. Assign the result to
#   factor_percentages.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    mapping = {'Economy (GDP per Capita)': 'Economy', 'Health (Life Expectancy)': 'Health',
               'Trust (Government Corruption)': 'Trust'}

    #  DataFrame with factor columns renamed.
    happiness2015 = happiness2015.rename(mapping, axis=1)
    factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity']
    factors_impact = happiness2015[factors].applymap(label, )

    v_counts_pct = factors_impact.apply(v_counts)

    percentages = Percentages(happiness2015)

    factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity', 'Dystopia Residual']
    factor_percentages = happiness2015[factors].apply(percentages)

    print(factor_percentages)


if __name__ == '__main__':
    main()
