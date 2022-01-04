# - Find the theoretical probability of getting a 5 when rolling a six-sided die. Assign your answer to p_5.
# - Tossing a coin twice has four possible outcomes (assume all the outcomes are equally likely):
#   - Heads on the first toss and heads on the second toss (HH).
#   - Heads on the first toss and tails on the second (HT).
#   - Tails on the first toss and heads on the second (TH).
#   - Tails on the first toss and tails on the second (TT).
# - Find:
#   - P(HT): Assign your result to p_ht.
#   - P(TT): Assign your result to p_tt.
def main():
    p_5 = 1 / 6
    p_ht = 1 / 4
    p_tt = 1 / 4
    print(p_5, p_ht, p_tt, sep='\n')


if __name__ == '__main__':
    main()
