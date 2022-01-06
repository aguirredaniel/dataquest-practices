# - Find the probability of getting at least one double-six in 24 throws of two six-sided dice (the two dice are thrown
#   simultaneously). Assign your answer to p_one_double_6. The table below shows all the outcomes of throwing two
#   six-sided dice.
def main():
    p_double_six = 1 / 6 ** 2
    p_non_double_six = 1 - p_double_six
    p_non_double_six_24 = p_non_double_six ** 24
    p_one_double_6 = 1 - p_non_double_six_24

    print(p_one_double_6)


if __name__ == '__main__':
    main()
