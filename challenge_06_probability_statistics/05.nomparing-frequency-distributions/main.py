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


# - Looking on our graph above, it's not easy to visualize where the average number of minutes is. Using the
#   plt.axvline() function, add a vertical line to demarcate the average point:
#   - The vertical line should be at point 497 on the x-axis.
#   - Use the label parameter of plt.axvline() to label it 'Average'. Display the label by running plt.legend().
#   - Specify plt.show() to display the plot.
def main():
    wnba = pd.read_csv('../data/wnba.csv')
    wnba['Exp_ordinal'] = pd.to_numeric(wnba['Experience'], errors='coerce').apply(experience_to_ordinal_scale)

    wnba['age_mean_relative'] = wnba['Age'].apply(lambda x: 'old' if x >= 27 else 'young')
    wnba['min_mean_relative'] = wnba['MIN'].apply(lambda x: 'average or above' if x >= 497 else 'below average')

    wnba[wnba.Age >= 27]['MIN'].plot.hist(histtype='step', label='Old', legend=True)
    wnba[wnba.Age < 27]['MIN'].plot.hist(histtype='step', label='Young', legend=True)
    plt.axvline(497, label='Average')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
