import matplotlib.pyplot as plt
import pandas as pd


def setup_plot_cumulative_cases(df: pd.DataFrame, country: str):
    """
    Setup a line graph for cumulative cases in specific Country.

    Parameters
    --------
    df : pd.DataFrame
        An pd.DataFrame for 'WHO_time_series.csv' dataset.
    country : str
        Country name (in camel case) for which the graph will be made.

    Examples
    --------
    >>> setup_plot_cumulative_cases(who_time_series, 'China')
    """
    df_country = df[df['Country'] == country]
    date_reported = df_country['Date_reported']
    cumulative_cases = df_country['Cumulative_cases']
    plt.plot(date_reported, cumulative_cases, label=country)


def plot_cumulative_cases(df: pd.DataFrame, country: str):
    """
    Plot a line graph for cumulative cases in specific Country.

    Parameters
    --------
    df : pd.DataFrame
        An pd.DataFrame for 'WHO_time_series.csv' dataset.
    country : str
        Country name (in camel case) for which the graph will be made.

    Examples
    --------
    >>> plot_cumulative_cases(who_time_series, 'China')
    """
    # df_country = df[df['Country'] == country]
    # date_reported = df_country['Date_reported']
    # cumulative_cases = df_country['Cumulative_cases']
    # plt.plot(date_reported, cumulative_cases)
    setup_plot_cumulative_cases(df, country)

    plt.title(f'{country}: Cumulative Reported Cases')
    plt.xlabel('Date')
    plt.ylabel('Number of cases')
    plt.legend()
    plt.show()


def plot_comparing_cumulative_cases(df: pd.DataFrame, countries: [str]):
    """
    Comparing a line graph for cumulative cases in specific Countries.

    Parameters
    --------
    df : pd.DataFrame
        An pd.DataFrame for 'WHO_time_series.csv' dataset.
    countries : str
        List if Country names (in camel case) for which the graphs will be made.

    Examples
    --------
    >>> plot_comparing_cumulative_cases(who_time_series, ['India', 'China','Indonesia')
    """
    for country in countries:
        setup_plot_cumulative_cases(df, country)

    plt.title(f'Comparing Cumulative Reported Cases')
    plt.xlabel('Date')
    plt.ylabel('Number of cases')
    plt.legend()
    plt.show()


# - Plot the evolution of cumulative cases for France, the United Kingdom, and Italy on the same graph.
# - Add a legend to the graph using plt.legend(). Use the labels France, The UK, and Italy.
# - Run your code without submitting the answer.
# - Which country has the greatest number of cases at the end of July? Assign your answer as a string to the variable
#   greatest_july — choose between the strings 'France', 'The UK', and 'Italy'.
# - Which country has the lowest number of cases at the end of July? Assign your answer as a string to the variable
#   lowest_july.
# - Which country shows the greatest increase during March? Assign your answer as a string to the variable
#   increase_march
def main():
    who_time_series = pd.read_csv('WHO_time_series.csv')

    # Initial exploring
    print(who_time_series.info())
    # Converting Date_reported column values to datetime data type.
    who_time_series['Date_reported'] = pd.to_datetime(who_time_series['Date_reported'], format='%Y-%m-%d')
    # Comparing cumulative_cases types of growth
    plot_comparing_cumulative_cases(who_time_series, ['France', 'The United Kingdom', 'Italy'])

    greatest_july = 'The UK'
    lowest_july = 'France'
    increase_march = 'Italy'


if __name__ == '__main__':
    main()
