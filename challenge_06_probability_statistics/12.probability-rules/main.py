# - An online betting company offers customers the possibility of betting on a variety of games and events (football,
#   tennis, hockey, horse races, car races, etc.). Based on historical data, the company knows the empirical
#   probabilities of the following events:
#   - Event F (a new customer's first bet is on football) — the probability is 0.26.
#   - Event T (a new customer's first bet is on tennis) — the probability is 0.11.
#   - Event "T and F" (a new customer's first bet is on both football and tennis) — the probability is 0.03.
# - Find the probability that a new customer's first bet is either on football or tennis. Assign your answer to p_f_or_t
#   You can't use theoretical probability formula to solve this, so you'll need to make use of the addition rule.
def main():
    p_f_or_t = 0.26 + 0.11 - 0.03
    print(p_f_or_t)


if __name__ == '__main__':
    main()
