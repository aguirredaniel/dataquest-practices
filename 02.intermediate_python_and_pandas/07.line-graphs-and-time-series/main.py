import matplotlib.pyplot as plt
import pandas as pd


def plot_cumulative_cases(df: pd.DataFrame, country: str):
    """
    Plots a line graph for cumulative cases in specific Country.

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
    df_country = df[df['Country'] == country]
    date_reported = df_country['Date_reported']
    cumulative_cases = df_country['Cumulative_cases']
    plt.plot(date_reported, cumulative_cases)
    plt.title(f'{country}: Cumulative Reported Cases')
    plt.xlabel('Date')
    plt.ylabel('Number of cases')
    plt.show()


# - In the code editor, we already wrote a function called plot_cumulative_cases() to help you plot line graphs more
#   easily. For example, plot_cumulative_cases('India') plots a line graph for cumulative cases in India. At the end of
#   the function's body, we also use plt.show() to "close" each graph and inform Matplotlib that the next graph we'll
#   built is a different one — we'll learn more about this soon.
# - Plot line graphs for Brazil, Iceland, and Argentina using the plot_cumulative_cases() function.
# - Determine the type of growth by examining the line graphs.
#   - Assign your answers to the variables brazil, iceland, and argentina.
#   - For example, assign the string 'linear' to brazil if you think Brazil shows linear growth.
#   - Choose between these three strings: 'linear', 'exponential', and 'logarithmic'.
def main():
    who_time_series = pd.read_csv('WHO_time_series.csv')

    # Initial exploring
    print(who_time_series.info())
    # Converting Date_reported column values to datetime data type.
    who_time_series['Date_reported'] = pd.to_datetime(who_time_series['Date_reported'], format='%Y-%m-%d')

    # Exploring cumulative_cases types of growth
    plot_cumulative_cases(who_time_series, 'Brazil')
    plot_cumulative_cases(who_time_series, 'Iceland')
    plot_cumulative_cases(who_time_series, 'Argentina')

    brazil = 'exponential'
    iceland = 'logarithmic'
    argentina = 'exponential'


if __name__ == '__main__':
    main()
