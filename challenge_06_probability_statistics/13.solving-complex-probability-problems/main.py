# - We're sampling without replacement from a standard 52-card deck. Find the probability of:
#   - Getting two kings in a row. Assign your answer to p_kk.
#   - Getting a seven of hearts, followed by a queen of diamonds. Assign your answer to p_7q.
#   - Getting a jack, followed by a queen of diamonds, followed by a king, followed by another jack. Assign your answer
#     to p_jqkj. This one is a bit tricky, so pay attention to the details of the question.
def main():
    p_kk = 4 / 52 * 3 / 51
    p_7q = 1 / 52 * 1 / 51
    p_jqkj = 4 / 52 * 1 / 51 * 4 / 50 * 3 / 49

    print(p_kk, p_7q, p_jqkj, sep='\n')


if __name__ == '__main__':
    main()
