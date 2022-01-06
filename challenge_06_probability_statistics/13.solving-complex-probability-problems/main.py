# - Find the probability of:
#   - Getting heads up 18 times in a row when flipping a fair coin. Assign your answer to p_18h.
#   - Getting a six three times in a row when throwing a fair six-sided die. Assign your answer to p_666.
#   - Not getting any six when throwing a fair six-sided die four times. Assign your answer to p_not_6.
def main():
    p_18h = 0.5 ** 18
    p_666 = (1 / 6) ** 3
    p_not_6 = (5 / 6) ** 4

    print(p_18h, p_666, p_not_6, sep='\n')


if __name__ == '__main__':
    main()
