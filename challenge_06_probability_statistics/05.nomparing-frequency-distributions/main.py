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


# - Using sns.boxplot(), generate a series of box plots to examine the distribution of player weight as a function of
#   player position. Place the Pos variable on the x-axis and the Weight variable on the y-axis.
# - Specify plt.show() to display the plot.
def main():
    wnba = pd.read_csv('../data/wnba.csv')
    wnba['Exp_ordinal'] = pd.to_numeric(wnba['Experience'], errors='coerce').apply(experience_to_ordinal_scale)

    wnba['age_mean_relative'] = wnba['Age'].apply(lambda x: 'old' if x >= 27 else 'young')
    wnba['min_mean_relative'] = wnba['MIN'].apply(lambda x: 'average or above' if x >= 497 else 'below average')

    sns.boxplot(x='Pos', y='Weight', data=wnba)
    plt.show()


if __name__ == '__main__':
    main()
