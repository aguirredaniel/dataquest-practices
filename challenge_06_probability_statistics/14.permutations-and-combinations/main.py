# - Find the probability of cracking a 4-digit PIN code using the code 8362. Assign your answer to p_crack_4.
# -0 Find the probability of cracking a 6-digit PIN code using the code 348821. Assign your answer to p_crack_6.
def permutation(n, k=None):
    """
    Calculate the nPk=n⋅(n−1)⋅(n−2)⋅…⋅(n−k+1) formula.

    Args:
        n: number of objects
        k: number of taking objects

    Returns:
        The n! (n factorial).

    Examples
    --------
    >>> permutation(5)
    120
    >>> permutation(52, 3)
    421200
    """
    if not k:
        k = n
    if k == 1:
        return n
    return n * permutation(n - 1, k - 1)


def main():
    p_crack_pass = 1 / permutation(127, 16)

    print(p_crack_pass)


if __name__ == '__main__':
    main()
