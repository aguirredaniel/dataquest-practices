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


# - Examine the distribution of the following two variables:
# - AST (number of assists).
# - FT% (percentage of free throws made out of all attempts).
# - Depending on the shape of the distribution, assign the string 'left skewed' or 'right skewed' to the following
#   variables:
#  - assists_distro for the AST column.
#  - ft_percent_distro for the FT% column.
# - For instance, if you think the AST variable has a right skewed distribution, your answer should be assists_distro =
#   'right skewed'.
def main():
    wnba = pd.read_csv('../data/wnba.csv')
    wnba['Exp_ordinal'] = pd.to_numeric(wnba['Experience'], errors='coerce').apply(experience_to_ordinal_scale)

    wnba['AST'].plot.hist()
    plt.show()
    wnba['FT%'].plot.hist()
    plt.show()

    ft_percent_distro, assists_distro = 'left skewed', 'right skewed'


if __name__ == '__main__':
    main()
