import pandas as pd


def label(factor, x):
    """
    Indicate whether the factor has a high impact on the happiness score or a low impact
    Args:
        x:
            Value to make comparation with factor value.
        factor:

    Returns:
        str: A label for impact of factor. Two possible values can be returned: High or Low

    Examples:
        >>> label(1.39651)
        'High'

        >>> label(0.90563)
        'Low'
    """
    if factor > x:
        return 'High'
    else:
        return 'Low'


# - Update label to take in another argument named x. If the element is greater than x, return 'High'. Otherwise, return
#   'Low'.
# - Then, use the apply method to apply label to the Economy column and set the x argument to 0.8. Save the result back
#   to economy_impact_apply.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    mapping = {'Economy (GDP per Capita)': 'Economy', 'Health (Life Expectancy)': 'Health',
               'Trust (Government Corruption)': 'Trust'}

    #  DataFrame with factor columns renamed.
    happiness2015 = happiness2015.rename(mapping, axis=1)

    economy_impact_apply = happiness2015['Economy'].apply(label, x=0.8)
    print(economy_impact_apply)


if __name__ == '__main__':
    main()
