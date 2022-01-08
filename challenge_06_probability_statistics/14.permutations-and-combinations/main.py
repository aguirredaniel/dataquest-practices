# - Find the probability of cracking a 4-digit PIN code using the code 8362. Assign your answer to p_crack_4.
# -0 Find the probability of cracking a 6-digit PIN code using the code 348821. Assign your answer to p_crack_6.
def main():
    four_digit_outcomes = 10 ** 4
    p_crack_4 = 1 / four_digit_outcomes

    six_digit_outcomes = 10 ** 6
    p_crack_6 = 1 / six_digit_outcomes

    print(p_crack_4, p_crack_6, sep='\n')


if __name__ == '__main__':
    main()
