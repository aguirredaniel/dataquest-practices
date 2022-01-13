# - P(M), the probability that a customer buys a mouse — assign your answer to p_m.
# - P(M|L), the probability that a customer buys a mouse given that they bought a laptop — assign your answer to
#   p_m_given_l.
# - P(M ∩ L), the probability that a customer buys both a mouse and a laptop — assign your answer to p_m_and_l.
# - P(M ∪ L), the probability that a customer buys a mouse or a laptop — assign your answer to p_m_or_l. Check the hint
#   if you don't remember how to calculate this.
def main():
    p_m = 515 / 2000
    p_l = 90 / 2000
    p_m_given_l = (32 / 2000) / p_l
    p_m_and_l = p_m_given_l * p_l
    p_m_or_l = p_m + p_l - p_m_and_l

    print(p_m, p_l, p_m_given_l, p_m_and_l, p_m_or_l, sep='\n')


if __name__ == '__main__':
    main()
