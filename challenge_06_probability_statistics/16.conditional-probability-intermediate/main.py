# - Find:
#   - P(M|LC) — assign your answer to p_m_given_non_l.
#   - P(LC|M) — assign your answer to p_non_l_given_m.
#   - P(M ∩ LC) — assign your answer to p_m_and_non_l.
#   - P(LC ∩ M) — assign your answer to p_non_l_and_m. Check the hint if you're not sure about exercises 3 and 4.
def main():
    p_m_given_non_l = 483 / 1910
    p_non_l_given_m = 483 / 515
    p_m_and_non_l = p_m_given_non_l * 1910 / 2000
    p_non_l_and_m = p_non_l_given_m * 515 / 2000

    print(p_m_given_non_l, p_non_l_given_m, p_m_and_non_l, p_non_l_and_m, sep='\n')


if __name__ == '__main__':
    main()
