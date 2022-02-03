def chi_squared(observed, expected):
    return (observed - expected) ** 2 / expected


# - Compute the chi-squared value for the observed values and the expected values.
# - Assign the result to chisq_gender_income.
def main():
    males_over50k = .241 * .67 * 32561
    males_under50k = 0.759 * .67 * 32561
    females_over50k = 0.241 * .33 * 32561
    females_under50k = 0.759 * .33 * 32561

    observed_values = [6662, 15128, 1179, 9592]
    expected_values = [males_over50k, males_under50k, females_over50k, females_under50k]

    chi_squareds = [chi_squared(observed, expected) for observed, expected in zip(observed_values, expected_values)]
    chisq_gender_income = sum(chi_squareds)

    print(chisq_gender_income)


if __name__ == '__main__':
    main()
