# - We roll a fair six-sided die three times and then randomly draw a card from a standard 52-card deck. One of the
#   outcomes is (6, 6, 6, ace of diamonds), which means getting three 6's in a row when we roll the die, followed by
#   drawing an ace of diamonds from the deck.
#   - Use the extended rule of product to calculate the total number of outcomes. Assign your answer to total_outcomes.
#   - Use total_outcomes to calculate the probability of getting (6, 6, 6, ace of diamonds) — three sixes in a row
#     followed by an ace of diamonds. Assign your answer to p_666_ace_diamonds.
#   - Use p_666_ace_diamonds to calculate the probability of getting anything but (6, 6, 6, ace of diamonds). Assign
#     your answer to p_no_666_ace_diamonds.
def main():
    total_outcomes = 6 ** 3 * 52
    p_666_ace_diamonds = 1 / 6 ** 3 * 1 / 52
    p_no_666_ace_diamonds = 1 - p_666_ace_diamonds

    print(total_outcomes, p_666_ace_diamonds, p_no_666_ace_diamonds, sep='\n')


if __name__ == '__main__':
    main()
