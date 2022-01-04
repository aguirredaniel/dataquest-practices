# - Assume all the outcomes of rolling a six-sided die have an equal chance of occurring. Calculate as proportion the
#   probability of the following events:
#   - We get an even number — assign your answer to p_even.
#   - We get an odd number different than 3 — assign your answer to p_odd_no_3.
#   - We get an odd number greater than 5 — assign your answer to p_odd_greater_5.
def main():
    p_even = 3 / 6
    p_odd_no_3 = 2 / 6
    p_odd_greater_5 = 0 / 6
    print(p_even, p_odd_no_3, p_odd_greater_5, sep='\n')


if __name__ == '__main__':
    main()
