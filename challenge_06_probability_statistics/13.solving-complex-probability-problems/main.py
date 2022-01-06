# - An advertisement company monitors the activity for a specific ad and shows it repeatedly to the same users (so a
#   single user sees the ad multiple times). Regardless of the number of times the ad is shown to a user, the
#   probability that the user clicks on the ad is 0.5. Find:
#   - The probability that a user doesn't click on the ad. Assign your answer to p_non_click.
#   - The probability that it takes two times or less for a user to click on the ad. Assign your answer to
#     p_two_or_less.
#   - The probability that it takes three times or more for a user to click on the ad. Assign your answer to
#     p_three_or_more.
def main():
    p_non_click = 1 - 0.5
    p_two_or_less = 3 / 4
    p_three_or_more = 1 - p_two_or_less

    print(p_two_or_less, p_three_or_more, sep='\n')


if __name__ == '__main__':
    main()
