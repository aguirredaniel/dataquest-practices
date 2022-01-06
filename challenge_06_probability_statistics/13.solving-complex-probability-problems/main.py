# - For rolling a fair six-sided die, find:
#   - The probability of getting a 6 two times in a row. Assign your result to p_6_6.
#   - The probability of getting a 3 on the first throw and a 2 on the second throw. Assign your result to p_3_2.
#   - The probability of getting an even number on both throws. Assign your result to p_even_even.
#   - The probability of getting a 1 on the first throw and an even number on the second throw. Assign your result to
#     p_1_even.
def main():
    p_6_6 = 1 / 6 * 1 / 6
    p_3_2 = 1 / 6 * 1 / 6
    p_even_even = 3 / 6 * 3 / 6
    p_1_even = 1 / 6 * 3 / 6

    print(p_6_6, p_3_2, p_even_even, p_1_even, sep='\n')

if __name__ == '__main__':
        main()
