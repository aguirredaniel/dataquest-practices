# - For our electronics store example, say new data is collected. We know that:
#   - The probability that a customer doesn't buy a set of laptop stickers is P(LSC) = 0.9821.
#   - The probability that a customer buys screen cleaning wipes given that they bought a set of laptop stickers is
#     P(CW | LS) = 0.0079.
#   - The probability that a customer buys a laptop given that they bought both a set of laptop stickers and screen
#     cleaning wipes is P(L | LS ∩ CW) = 0.2908.
# - Assume events LS, CW, and L are dependent and calculate P(LS ∩ CW ∩ L). Assign your answer to p_ls_and_cw_and_l.
def main():
    p_non_ls = 0.9821
    p_cw_given_ls = 0.0079
    p_l_given_ls_and_cw = 0.2908

    p_ls = 1 - p_non_ls
    p_ls_and_cw_and_l = p_ls * p_cw_given_ls * p_l_given_ls_and_cw

    print(p_ls_and_cw_and_l)


if __name__ == '__main__':
    main()
