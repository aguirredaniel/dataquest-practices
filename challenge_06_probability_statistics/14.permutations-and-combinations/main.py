# - Consider the composite experiment E1E2, where E1 is rolling a fair six-sided die once, and E2 is rolling the same
#   die again. One of the outcomes of E1E2 could be (1, 6), which means we get a 1 for the first roll and a 6 for the
#   second one.
#   - Use the rule of product to calculate the total number of outcomes. Assign your answer to n_outcomes.
#   - Use n_outcomes to calculate the probability of getting a (6,6). Assign your answer to p_six_six. Check the hint if
#     you have difficulties calculating this.
#    - Use n_outcomes to calculate the probability of not getting a (5,5) and assign your answer to p_not_five_five.
def main():
    n_outcomes = 6 * 6
    p_six_six = 1 / 6 ** 2
    p_not_five_five = 1 - 1 / 6 ** 2

    print(n_outcomes, p_six_six, p_not_five_five, sep='\n')


if __name__ == '__main__':
    main()
