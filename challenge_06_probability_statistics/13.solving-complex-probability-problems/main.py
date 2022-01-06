# - Find the probability that it takes four flips or more for a coin to land heads up (let's call this event "B").
#   - Begin with finding the probability of the event non-B, which is equivalent to finding the probability that we'll
#     get at least one heads if we flip a coin three times. Assign your result to p_non_b.
#   - Now use p_non_b to find the probability of B. Assign your result to p_b.
def main():
    p_non_b = 7 / 8
    p_b = 1 - p_non_b

    print(p_non_b, p_b, sep='\n')


if __name__ == '__main__':
    main()
