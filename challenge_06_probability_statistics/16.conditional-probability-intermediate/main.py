# - Using the two rules we learned above, find:
#   - P(BC|M), and assign your answer to p_non_b_given_m.
#   - P(CC|L), and assign your answer to p_non_c_given_l.
#   - P(B|C), and assign your answer to p_b_given_c.
#   - P(B|MC), and assign your answer to p_b_given_non_m. If you think you can't calculate the probability using any of
#     the two rules above, assign the string 'not possible' to the same variable p_b_given_non_m.
def main():
    p_b_given_m = 0.1486
    p_c_given_l = 0.0928
    p_non_b_given_c = 0.7622

    p_non_b_given_m = 1 - p_b_given_m
    p_non_c_given_l = 1 - p_c_given_l
    p_b_given_c = 1 - p_non_b_given_c

    p_b_given_non_m = 'not possible'


if __name__ == '__main__':
    main()
