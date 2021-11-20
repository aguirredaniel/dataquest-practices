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


# - For each segment, generate a frequency distribution table for the Pos variable.
# - For the rookies segment, assign the frequency distribution table to a variable named rookie_distro.
# - For the little experience segment, assign the table to little_xp_distro.
# - For the experienced segment, assign the table to experienced_distro.
# - For the very experienced segment, assign the table to very_xp_distro.
# - For the veterans segment, assign the table to veteran_distro.
# - Print all the tables and analyze them comparatively to determine whether there are any clear patterns in the
#   distribution of player position depending on the level of experience.
def main():
    wnba = pd.read_csv('../data/wnba.csv')
    wnba['Exp_ordinal'] = pd.to_numeric(wnba['Experience'], errors='coerce').apply(experience_to_ordinal_scale)

    rookies = wnba[wnba['Exp_ordinal'] == 'Rookie']
    little_xp = wnba[wnba['Exp_ordinal'] == 'Little experience']
    experienced = wnba[wnba['Exp_ordinal'] == 'Experienced']
    very_xp = wnba[wnba['Exp_ordinal'] == 'Very experienced']
    veterans = wnba[wnba['Exp_ordinal'] == 'Veteran']

    frequency_distributions = [df['Pos'].value_counts() for df in [rookies, little_xp, experienced, very_xp, veterans]]
    print(frequency_distributions, sep='\n')


if __name__ == '__main__':
    main()
