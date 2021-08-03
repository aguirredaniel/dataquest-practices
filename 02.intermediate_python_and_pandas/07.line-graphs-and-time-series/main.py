import matplotlib.pyplot as plt


# - Plot a line graph using plt.plot().
#   - month_number gives the x-coordinates
#   - new_deaths gives the y_coordinates
# - Using plt.title(), add the title 'New Reported Deaths By Month (Globally)'. For answer-checking purposes, make sure
#   the title you add is exactly the same (the answer-checking is case sensitive).
# - Using plt.xlabel(), add the x-label 'Month Number'.
# - Using plt.ylabel(), add the y-label 'Number Of Deaths'.
# - Display the plot using plt.show().
def main():
    month_number = [1, 2, 3, 4, 5, 6, 7]
    new_deaths = [213, 2729, 37718, 184064, 143119, 136073, 165003]

    plt.plot(month_number, new_deaths)
    plt.title('New Reported Deaths By Month (Globally)')
    plt.xlabel('Month Number')
    plt.ylabel('Number Of Deaths')
    plt.show()


if __name__ == '__main__':
    main()
