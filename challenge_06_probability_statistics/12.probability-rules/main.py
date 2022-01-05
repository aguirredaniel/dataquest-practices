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
# - Using the table above, find for the same experiment the probability of the following events:
#   - The sum is either 5 or 9 — assign your answer to p_5_or_9.
#   - The sum is either even or less than 2 — assign your answer to p_even_or_less_2.
#   - The sum is either 4 or a multiple of 3 — assign your answer to p_4_or_3_multiple. Check the hint if you don't
#     remember what a multiple is.
def main():
    p_5_or_9 = 8 / 36
    p_even_or_less_2 = 18 / 36
    p_4_or_3_multiple = 15 / 36

    print(p_5_or_9, p_even_or_less_2, p_4_or_3_multiple, sep='\n')


if __name__ == '__main__':
    main()
