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


# - Consider the quartiles of the Games Played variable:
# - Find the interquartile range, and assign the result to a variable named iqr.
# - Using a factor of 1.5, calculate the lower and upper bound outside which values are considered outliers.
#   -Assign the value of the lower bound to a variable named lower_bound.
#   - Assign the upper bound to a variable named upper_bound.
# - Find how many values in the distribution are outliers.
#   - Assign the number of outliers below the lower bound to a variable named outliers_low.
#  - Assign the number of outliers above the upper bound to a variable named outliers_high.
# - Plot a boxplot to check whether your answers are sensible.
#   - Specify plt.show() to display the plot.
def main():
    wnba = pd.read_csv('../data/wnba.csv')
    wnba['Exp_ordinal'] = pd.to_numeric(wnba['Experience'], errors='coerce').apply(experience_to_ordinal_scale)

    games_played = wnba['Games Played']
    quartiles = games_played.describe()[4:-1]
    upper_quartile = quartiles[-1]
    lower_quartile = quartiles[0]
    factor = 1.5
    iqr = upper_quartile - lower_quartile
    iqr_factor = (iqr * factor)
    lower_bound = lower_quartile - iqr_factor
    upper_bound = upper_quartile + iqr_factor

    outliers_low = games_played[games_played < lower_bound].size
    outliers_high = games_played[games_played > upper_bound].size

    sns.boxplot(x=games_played)
    plt.show()


if __name__ == '__main__':
    main()
