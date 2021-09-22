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


# - Create a function that calculates the percentage of 'High' and 'Low' values in each column.
#   - Create a function named v_counts that accepts one parameter called col.
#   - Use the Series.value_counts() method to calculate the value counts for col. Assign the result to num.
#   - Use the Series.size attribute to calculate the number of rows in the column. Assign the result to den.
# - Divide num by den and return the result.
# - Use the df.apply() method to apply the v_counts function to all of the columns in factors_impact. Assign the result
#   to v_counts_pct.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    mapping = {'Economy (GDP per Capita)': 'Economy', 'Health (Life Expectancy)': 'Health',
               'Trust (Government Corruption)': 'Trust'}

    #  DataFrame with factor columns renamed.
    happiness2015 = happiness2015.rename(mapping, axis=1)
    factors = ['Economy', 'Family', 'Health', 'Freedom', 'Trust', 'Generosity']
    factors_impact = happiness2015[factors].applymap(label, )

    v_counts_pct = factors_impact.apply(v_counts)

    print(v_counts_pct)


if __name__ == '__main__':
    main()
