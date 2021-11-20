import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def experience_to_ordinal_scale(experience: int) -> str:
    """
     Converts number of years a player has played (experience) to ordinal scale value:
    Args:
        experience:
            Experience in years in WNBA
    Returns:
        One of the next ordinal scale values:
        - Rookie (0)
        - Little experience (1-3)
        - Experienced (4-5)
        - Very experienced (5-10)
        - Veteran (>10)
    Example:
        >>> experience_to_ordinal_scale(2)
        'Little experience'
    """

    if pd.isna(experience):
        return 'Rookie'

    if experience and experience <= 3:
        return 'Little experience'

    if experience <= 5:
        return 'Experienced'

    if experience <= 10:
        return 'Very experienced'

    return 'Veteran'


# - Usng sns.countplot(), generate a grouped bar plot similar to the one above.
#  - Place the Exp_ordinal variable on the x-axis.
#  - Generate the bar plots for the Pos variable. The data set is stored in wnba variable.
#  - Using the order parameter of sns.countplot(), order the values on the x-axis in ascending order. The order
#    parameter takes in a list of strings, so you should use order = ['Rookie', 'Little experience', ..........].
#  - Using the hue_order parameter, order the bars of each bar plot in ascending alphabetic order. hue_order takes in a
#    list of strings, so you can use hue_order = ['C', 'F', ......].
def main():
    wnba = pd.read_csv('../data/wnba.csv')
    wnba['Exp_ordinal'] = pd.to_numeric(wnba['Experience'], errors='coerce').apply(experience_to_ordinal_scale)

    sns.countplot(
        x='Exp_ordinal', hue='Pos', data=wnba,
        hue_order=['C', 'F', 'F/C', 'G', 'G/F'],
        order=['Rookie', 'Little experience', 'Experienced', 'Very experienced', 'Veteran'])

    plt.show()


if __name__ == '__main__':
    main()
