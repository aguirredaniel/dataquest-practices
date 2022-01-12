# - A fair six-sided die is rolled. All we know is that the number we got is less than 5. Calculate:
#   - The probability of getting a 3. Assign your answer to p_3.
#   - The probability of getting a 6. Assign your answer to p_6.
#   - The probability of getting an odd number. Assign your answer to p_odd.
#   - The probability of getting an even number. Assign your answer to p_even.
def main():
    p_3 = 1 / 4
    p_6 = 0
    p_odd = 2 / 4
    p_even = 2 / 4
    print(p_3, p_6, p_odd, p_even, sep='\n')


if __name__ == '__main__':
    main()
