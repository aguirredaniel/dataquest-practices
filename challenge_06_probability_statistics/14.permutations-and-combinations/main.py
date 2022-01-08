# - Use the factorial() and permutation() functions to calculate the number of unique 5-card arrangements when drawing
#   without replacement from a standard 52-card deck. Assign your answer to a variable named c.
# - Calculate the probability of getting a 5-card hand with four aces and a seven of diamonds (assume we're drawing
#   randomly and without replacement from the deck). Assign your answer to p_aces_7.
# -  For a state lottery, six numbers are drawn randomly and without replacement from a set containing numbers from 1 to
#    49. Using the factorial() and the permutation() functions, find the total number of unique 6-number arrangements
#    that could result. Assign your answer to c_lottery.
# - Calculate the probability of winning the big prize for this state lottery provided you use the numbers (3, 20, 37,
#   44, 45, 49) — the big prize means the numbers match exactly those resulted from the official drawing.
#   - Assign your answer to p_big_prize.
#   - Print p_big_prize to see what are the chances of winning the big prize and think whether you'd recommend spending
#     money on lottery to a close friend
def factorial(n):
    """
    Calculate the factorial of n (n!)
    Args:
        n: numeric value

    Returns:
        The n!.

    Examples
    ________
    >>> factorial(5)
    120
    """
    if n == 2:
        return 2
    return n * factorial(n - 1)


def permutation(n, k):
    """
    Calculate the nPk=n⋅(n−1)⋅(n−2)⋅…⋅(n−k+1) formula.

    Args:
        n: number of objects
        k: number of taking objects

    Returns:
        The permutation of n (nPk)

    Examples
    --------
    >>> permutation(52, 3)
    421200
    """
    return factorial(n) / factorial(n - k)


def main():
    c = permutation(52, 5) / factorial(5)
    p_aces_7 = 1 / c

    c_lottery = permutation(49, 6) / factorial(6)
    p_big_prize = 1 / c_lottery

    print(c, p_aces_7, c_lottery, p_big_prize, sep='\n')


if __name__ == '__main__':
    main()
