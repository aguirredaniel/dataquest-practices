# - Find whether the following events are independent or not (check the hint if you don't know how to solve this):
#   - Events L and M — assign the string 'independent' to a variable named l_and_m if the events are independent,
#     otherwise assign the string 'dependent'.
#   - Events L and MC — assign the string 'independent' to a variable named l_and_non_m if the events are independent,
#     otherwise assign the string 'dependent'.
# - Use the formulas we learned to calculate (you could also calculate the probabilities just by looking at the table in
#   this case, but try to use the formulas):
#   - P(L ∩ M) — assign your answer to p_l_and_m.
#   - P(L ∩ MC) — assign your answer to p_l_and_non_m.
def main():
    l_and_m = 'dependent'
    l_and_non_m = 'dependent'

    p_l_and_m = 515 / 2000 * 32 / 515
    p_l_and_non_m = 1485 / 2000 * 58 / 1485

    print(p_l_and_m, p_l_and_non_m, sep='\n')


if __name__ == '__main__':
    main()
