# - Find the probability of cracking a 4-digit PIN code using the code 8362. Assign your answer to p_crack_4.
# -0 Find the probability of cracking a 6-digit PIN code using the code 348821. Assign your answer to p_crack_6.
def factorial(n, k=None):
    """
    Calculate the nPk=n⋅(n−1)⋅(n−2)⋅…⋅(n−k+1) formula.

    Args:
        n: number of objects
        k: number of taking objects

    Returns:
        The n! (n factorial).

    Examples
    --------
    >>> factorial(5)
    120
    >>> factorial(52, 3)
    421200
    """
    if not k:
        k = n
    if k == 1:
        return n
    return n * factorial(n - 1, k - 1)


def main():
    perm_3_52 = factorial(52, 3)
    perm_4_20 = factorial(20, 4)
    perm_4_27 = factorial(27, 4)

    print(perm_3_52, perm_4_20, perm_4_27, sep='\n')


if __name__ == '__main__':
    main()
