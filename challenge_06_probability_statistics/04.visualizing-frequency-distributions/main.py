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


# - Examine the distribution of the following variables, trying to determine which one resembles the most a normal
#   distribution:
#   - Age
#   - Height
#   - MIN
# - Assign to the variable normal_distribution the name of the variable (as a string) whose distribution resembles the
#   most a normal one.
# - For instance, if you think the MIN variable is the correct answer, then your answer should be normal_distribution =
#   'MIN'.
def main():
    wnba = pd.read_csv('../data/wnba.csv')
    wnba['Exp_ordinal'] = pd.to_numeric(wnba['Experience'], errors='coerce').apply(experience_to_ordinal_scale)

    for column in ['Age', 'Height', 'MIN']:
        wnba[column].plot.hist(title=column)
        plt.show()

    normal_distribution = 'Height'


if __name__ == '__main__':
    main()
