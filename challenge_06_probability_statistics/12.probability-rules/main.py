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
#   - The sum is either 2 or 4. Assign the probability as a proportion to p_2_or_4.
#    - The sum is either 12 or 13. Assign the probability as a proportion to p_12_or_13.
def main():
    p_2_or_4 = 4 / 36
    p_12_or_13 = 1 / 36
    print(p_2_or_4, p_12_or_13, sep='\n')


if __name__ == '__main__':
    main()
