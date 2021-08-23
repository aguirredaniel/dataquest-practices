import pandas as pd
import matplotlib.pyplot as plt


# - Create a line plot using the ggplot style.
#   - The x-coordinates are [2, 4, 6].
#   - The y-coordinates are [10, 15, 5].
#   - Close and display the plot using plt.show().
# - Create a line plot using the default style.
#   - The coordinates are the same as above.
#   - Close and display the plot using plt.show().
def main():
    plt.style.use('ggplot')
    plt.plot([2, 4, 6],
             [10, 15, 5])
    plt.show()

    plt.style.use('default')
    plt.plot([2, 4, 6],
             [10, 15, 5])
    plt.show()


if __name__ == '__main__':
    main()
