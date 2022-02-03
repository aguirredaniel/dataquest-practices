# - Using the expected proportions in the table above, calculate the expected values for each of the 4 cells in the
#   table.
# - Calculate the expected value for Males who earn >50k, and assign to males_over50k.
# - Calculate the expected value for Males who earn <=50k, and assign to males_under50k.
# - Calculate the expected value for Females who earn >50k, and assign to females_over50k.
# - Calculate the expected value for Females who earn <=50k, and assign to females_under50k.
def main():
    males_over50k = .241 * .67 * 32561
    males_under50k = 0.759 * .67 * 32561
    females_over50k = 0.241 * .33 * 32561
    females_under50k = 0.759 * .33 * 32561

    print(males_over50k, males_under50k, females_over50k, females_under50k, sep='\n')


if __name__ == '__main__':
    main()
