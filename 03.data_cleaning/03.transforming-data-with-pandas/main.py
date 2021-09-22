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


# - Use the Series.map() method to apply the label function to the Economy column in happiness2015. Assign the result to
#   economy_impact_map.
# - Use the Series.apply() method to apply the label function to the Economy column. Assign the result to
#   economy_impact_apply.
# - Use the following code to check if the methods produce the same result:
#   economy_impact_map.equals(economy_impact_apply). Assign the result to a variable named equal.
def main():
    happiness2015 = pd.read_csv('World_Happiness_2015.csv')
    mapping = {'Economy (GDP per Capita)': 'Economy', 'Health (Life Expectancy)': 'Health',
               'Trust (Government Corruption)': 'Trust'}

    #  DataFrame with factor columns renamed.
    happiness2015 = happiness2015.rename(mapping, axis=1)

    economy_impact_map = happiness2015['Economy'].map(label)
    economy_impact_apply = happiness2015['Economy'].apply(label)

    equal = economy_impact_map.equals(economy_impact_apply)

    print(equal)


if __name__ == '__main__':
    main()
