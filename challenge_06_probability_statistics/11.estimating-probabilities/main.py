from numpy.random import seed, randint


# - For this exercise, we already defined the function coin_toss() and the variables probabilities and heads. We're
#   going to repeat the coin toss 10,000 times, and for each toss we want to save the value of P(H) up to that point.
# - For each of the 10,000 iterations of a for loop:
#   - Save the outcome of the coin_toss() function to a variable named outcome.
#   - If outcome stores the string 'HEAD', then increase the value of heads by 1.
#   - Divide heads by n to get the current value of P(H). Assign the value to current_probability.
#     - n comes from for n in range(1, 10001)
#   - Append current_probability to the list probabilities. The probabilities should be expressed as proportions, not
#     percentages.
#  - Print the first and last 10 values in probabilities to inspect the evolution of P(H). What do you observe? We'll
#    talk more about this on the next screen.
def coin_toss():
    return 'HEAD' if randint(0, 2) else 'TAIL'


def main():
    seed(1)
    probabilities = []
    heads = 0

    for n in range(1, 10001):
        outcome = coin_toss()

        if outcome == 'HEAD':
            heads += 1

        probability = heads / n
        probabilities.append(probability)

    print(probabilities[:10], probabilities[-10:], sep='\n')


if __name__ == '__main__':
    main()
