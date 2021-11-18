import matplotlib.pyplot as plt
import pandas as pd


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


# - Generate a frequency table for the Exp_ordinal variable.
# - Sort the table by unique labels in an ascending order.
# - Use the Series.plot.barh() method to generate the horizontal bar plot.
# - Add the following title to the plot: "Number of players in WNBA by level of experience"
def main():
    wnba = pd.read_csv('../data/wnba.csv')
    wnba['Exp_ordinal'] = pd.to_numeric(wnba['Experience'], errors='coerce').apply(experience_to_ordinal_scale)
    wnba['Exp_ordinal'].value_counts().iloc[[-2, 0, 2, 1, -1]] \
        .plot.barh(title='Number of players in WNBA by level of experience')
    plt.show()


if __name__ == '__main__':
    main()
