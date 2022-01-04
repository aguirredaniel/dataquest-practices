# - Just like in our example above, we tossed a coin 100 times and got heads 56 times. Calculate the probability of
#    getting tails using the formula above and assign the result to p_tail.
# - We rolled a regular six-sided die 200 times and:
#   - We got a six 28 times. Calculate the probability of getting a 6 when rolling a six-sided die. Assign the result to
#     p_six.
#   - We got an odd number (a 1, a 3, or a 5) 102 times. Calculate the probability of getting an odd number when rolling
#     a six-sided die. Assign the result to p_odd.
# - Print p_tail, p_six, and p_odd to examine the probabilities.
def main():
    p_tail = 44 / 100
    p_six = 28 / 200
    p_odd = 102 / 200

    print(p_tail, p_six, p_odd, sep='\n')


if __name__ == '__main__':
    main()
