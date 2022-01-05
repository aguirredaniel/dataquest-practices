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
# - Use the table above to find the probability of the following events:
#   - The sum of the two rolls is 6. Assign the probability to p_sum_6.
#   - The sum of the two rolls is lower than 15. Assign the probability to p_lower_15.
#   - The sum of the two rolls is greater than 13. Assign the probability to p_greater_13.
def main():
    p_sum_6 = 5 / 36
    p_lower_15 = 36 / 36
    p_greater_13 = 0 / 36

    print(p_sum_6, p_lower_15, p_greater_13, sep='\n')


if __name__ == '__main__':
    main()
