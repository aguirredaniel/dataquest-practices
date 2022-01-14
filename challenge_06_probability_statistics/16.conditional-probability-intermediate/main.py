# - For our electronics store example, say new data is collected, and we know that:
#   - The probability that a customer buys an electric toothbrush is P(ET) = 0.0432.
#   - The probability that a customer buys an electric toothbrush is P(ET) = 0.0432.
#   - The probability that a customer buys an air conditioning system is P(AC) = 0.0172
#   - The probability that a customer buys a PlayStation is P(PS) = 0.0236.
#  - Assuming events ET, AC, and PS are mutually independent, calculate:
#   - P(ET ∩ PS) — assign your answer to p_et_and_ps.
#   - P(ET ∩ AC) — assign your answer to p_et_and_ac.
#   - P(AC ∩ PS) — assign your answer to p_ac_and_ps.
#   - P(ET ∩ AC ∩ PS) — assign your answer to p_et_and_ac_and_ps.
def main():
    p_et = 0.0432
    p_ac = 0.0172
    p_ps = 0.0236

    p_et_and_ps = p_et * p_ps
    p_et_and_ac = p_et * p_ac
    p_ac_and_ps = p_ac * p_ps
    p_et_and_ac_and_ps = p_et * p_ac * p_ps

    print(p_et_and_ps, p_et_and_ac, p_ac_and_ps, p_et_and_ac_and_ps, sep='\n')


if __name__ == '__main__':
    main()
