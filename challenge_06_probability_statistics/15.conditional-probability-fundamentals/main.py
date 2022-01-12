# - A student is randomly selected from a class. All we know is that he was born during winter. Assume the winter months
#  are December, January, and February and ignore the fact that these three months have different number of days. Find:
#   - The probability that he was born in December. Assign your answer to p_december.
#   - The probability that he was born during summer. Assign your answer to p_summer.
#   - The probability that he was born in a month which ends in letter "r" — "September", for instance, ends in "r",
#     while "April" doesn't. Assign your answer to p_ends_r.
def main():
    p_december = 1 / 3
    p_summer = 0
    p_ends_r = 1 / 3
    print(p_december, p_summer, p_ends_r, sep='\n')


if __name__ == '__main__':
    main()
