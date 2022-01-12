# - Consider rolling a fair six-sided die once and calculate:
#   - The probability of getting a 2. Assign your answer to p_2.
#   - The probability of getting an odd number (1, 3, or 5). Assign your answer to p_odd.
#   - The probability of getting a 2 or a 4, Assign your answer to p_2_or_4.
def main():
    p_2 = 1 / 6
    p_odd = 3 / 6
    p_2_or_4 = 2 / 6

    print(p_2, p_odd, p_2_or_4, sep='\n')


if __name__ == '__main__':
    main()
