import numpy as np
import matplotlib.pyplot as plt


# -For each category (White, Black, Asian-Pac-Islander, Amer-Indian-Eskimo, and Other):
# - compute the difference between the expected and observed counts,
# - square the difference,
# - divide by the expected value,
# - append each result to a list, and
# - sum the values in the list and assign the result to race_chisq.
def chi_squared(observed, expected):
    return (observed - expected) ** 2 / expected


def main():
    table = [(27816, 26146.5), (3124, 3939.9), (1039, 944.3),
             (311, 260.5), (271, 1269.8), ]

    chi_squareds = (chi_squared(*sample) for sample in table)
    race_chisq = sum(chi_squareds)

    print(race_chisq)


if __name__ == '__main__':
    main()
