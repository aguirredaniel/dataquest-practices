import pandas as pd


# - Use the Age variable along with Series.describe() to answer the following questions:
#   - What's the upper quartile of the Age variable? Assign your answer to a variable named age_upper_quartile.
#   - What's the middle quartile of the Age variable? Assign your answer to a variable named age_middle_quartile.
#   - What's the 95th percentile of the Age variable? Assign your answer to a variable named age_95th_percentile.
# - Indicate the truth value of the following sentences:
#   - A percentile is a value of a variable, and it corresponds to a certain percentile rank in the distribution of that
#     variable. (If you think this is true, assign True (boolean, not string) to a variable named question1, otherwise
#     assign False.)
#   - A percentile rank is a numerical value from the distribution of a variable. (Assign True or False to question2.)
#   - The 25th percentile is the same thing as the lower quartile, and the upper quartile is the same thing as the third
#     quartile. (Assign True or False to question3)
def main():
    pd.options.display.max_rows = 200
    pd.options.display.max_columns = 50

    wnba = pd.read_csv('../data/wnba.csv')

    age_describe = wnba['Age'].describe(percentiles=[.75, .50, .95])
    age_middle_quartile, age_upper_quartile, age_95th_percentile = age_describe[4:-1]

    question1, question2, question3 = True, False, True
    print(age_upper_quartile, age_middle_quartile, age_95th_percentile)


if __name__ == '__main__':
    main()
