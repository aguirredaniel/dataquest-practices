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


# - Generate a grouped bar plot to confirm or reject our hypothesis. Using sns.countplot():
#   - Place the age_mean_relative variable on the x-axis. The age_mean_relative and min_mean_relative are already
#     defined.
#   - Generate the frequency distributions for the min_mean_relative variable.
# - Analyze the graph and determine whether the data confirms or rejects our hypothesis. If it's a confirmation assign
#   the string 'confirmation' to a variable named result. If it's a rejection, assign the string 'rejection' to the
#   variable result.
def main():
    wnba = pd.read_csv('../data/wnba.csv')
    wnba['Exp_ordinal'] = pd.to_numeric(wnba['Experience'], errors='coerce').apply(experience_to_ordinal_scale)

    wnba['age_mean_relative'] = wnba['Age'].apply(lambda x: 'old' if x >= 27 else 'young')
    wnba['min_mean_relative'] = wnba['MIN'].apply(lambda x: 'average or above' if x >= 497 else 'below average')

    sns.countplot(
        x='age_mean_relative', hue='min_mean_relative', data=wnba)

    plt.show()

    result = 'rejection'

if __name__ == '__main__':
    main()
