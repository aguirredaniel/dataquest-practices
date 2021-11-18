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


# - Generate a histogram for the Games Played variable, and customize it in the following way:
# - Each bin must cover an interval of 4 games. The first bin must start at 1, the last bin must end at 32.
# - Add the title "The distribution of players by games played".
# - Add a label to the x-axis named "Games played".
def main():
    wnba = pd.read_csv('../data/wnba.csv')
    wnba['Exp_ordinal'] = pd.to_numeric(wnba['Experience'], errors='coerce').apply(experience_to_ordinal_scale)

    wnba['Games Played'].plot.hist(
        range=(1, 32), bins=8, title='The distribution of players by games played'
    )
    plt.xlabel('Games played')
    plt.show()


if __name__ == '__main__':
    main()
