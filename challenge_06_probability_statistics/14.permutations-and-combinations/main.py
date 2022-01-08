# - Find the probability of cracking a 4-digit PIN code using the code 8362. Assign your answer to p_crack_4.
# -0 Find the probability of cracking a 6-digit PIN code using the code 348821. Assign your answer to p_crack_6.
def factorial(n):
    """
    Calculate the n factorial.

    Args:
        n: numeric value

    Returns:
        The n! (n factorial).

    Examples
    --------
    >>> factorial(5)
    120
    """
    if n == 2:
        return 2
    return n * factorial(n - 1)


def main():
    letters = {"a", "b", "j", "k", "x", "y"}
    permutations_1 = factorial(len(letters))
    permutations_2 = factorial(52)

    print(permutations_1, permutations_2, sep='\n')


if __name__ == '__main__':
    main()
