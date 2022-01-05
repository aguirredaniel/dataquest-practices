# For the following exercise, we'll consider a random experiment where we roll a fair six-sided die two times ("fair"
# means all outcomes have equal chances of occurring). The sample space of this experiment has 36 possible outcomes (all
# the sequences of numbers we can get from the two throws):
# E = {(1,1), (1,2), (1,3), ....., (3,1), (3,2), ....., (6,1), (6,2) }
# For each outcome, we sum up the two numbers and get the following sums:
#       2  3  4  5  6  7
#       3  4  5  6  7  8
#       .  .  .  .  .  .
#       .  .  .  .  .  .
#       7 8 9 10, 11, 12
# - Make sure you've read the instructions above and calculate (notice that for this exercise we're considering a single
#   die, not the sum of two dice):
#   - P(C) — assign your answer to p_c. C = {2, 4, 6} — getting an even number
#   - P(D) — assign your answer to p_d. D = {4, 5, 6} — getting a number greater than 3
# - The event "getting a number that is either even or greater than 3" corresponds to the event "C or D". Calculate:
#   - P(C or D) using the addition rule — assign your answer to p_c_d_addition. Check the hint if you're not sure about
#     the outcomes corresponding to the event "C or D".
#   - P(C or D) using the formula we've been using to compute theoretical probabilities (the number of successful
#     outcomes divided by the number of possible outcomes) — assign your answer to p_c_d_formula.
# - Print p_c_d_addition and p_c_d_formula. Why do you think we see different results (we'll explain this on the next
#   screen)?
def main():
    p_c = 3 / 6
    p_d = 3 / 6
    p_c_d_addition = 6 / 6
    p_c_d_formula = 4 / 6

    print(p_c, p_d, p_c_d_addition, p_c_d_formula, sep='\n')


if __name__ == '__main__':
    main()
