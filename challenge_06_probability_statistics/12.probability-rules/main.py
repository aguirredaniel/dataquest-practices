# - Based on historical data, the company knows the empirical probabilities of the following events:
#   - Event H (a new customer's first bet is on hockey) — the probability is 0.08.
#   - Event C (a new customer's first bet is on car races) — the probability is 0.11.
#   - Event "H or C" (a new customer's first bet is either on hockey or car races) — the probability is 0.17.
# - Find the probability that a new customer's first bet is on both hockey and car races. Assign your answer to
#   p_h_and_c. Check the hint if you get stuck.
def main():
    p_h_and_c = 0.08 + 0.11 - 0.17
    print(p_h_and_c)


if __name__ == '__main__':
    main()
