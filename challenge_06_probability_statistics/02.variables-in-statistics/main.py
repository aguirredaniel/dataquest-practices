import pandas
import pandas as pd


# - Add the variables measured on a nominal scale to a list named nominal_scale, and sort the elements in the list
#   alphabetically (the sorting helps us with answer checking).
# - Notice that we've added a new variable named Height_labels. Instead of showing the height in centimeters, the new
#   variable shows labels like "short", "medium", or "tall". By considering the principles that characterize the nominal
#   scale, think whether the new Height_labels variable should be included in your nominal_scale list.
def main():
    nominal_scale = sorted(['Name', 'Team', 'Pos', 'Birth_Place', 'College'])


if __name__ == '__main__':
    main()
