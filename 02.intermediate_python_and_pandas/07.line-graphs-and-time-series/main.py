import matplotlib.pyplot as ptl


# - Import the pyplot submodule as plt.
# - Plot a line graph using plt.plot(), where month_number gives the x-coordinates, and new_deaths gives the
#   y_coordinates.
# - Display the plot using plt.show().
def main():
    month_number = [1, 2, 3, 4, 5, 6, 7]
    new_deaths = [213, 2729, 37718, 184064, 143119, 136073, 165003]

    ptl.plot(month_number, new_deaths)
    ptl.show()


if __name__ == '__main__':
    main()
