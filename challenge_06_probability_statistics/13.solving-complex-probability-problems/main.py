# - An advertisement company runs a quick test and shows two ads on the same web page (ad "A" and ad "B") to 100 users.
#   At the end of the trial, they found:
#   - 12 users clicked on ad "A"
#   - 17 users clicked on ad "B"
#   - 3 users clicked on both ad "A" and ad "B"
# - Find:
#   - The empirical probability that a user clicks on ad "A." Assign your result to p_a.
#   - The empirical probability that a user clicks on ad "B." Assign your result to p_b.
#   - The empirical probability that a user clicks on both ad "A" and ad "B." Assign your result to p_a_and_b.
#   - The probability that a user clicks on either ad "A" or ad "B." Assign your result to p_a_or_b. For this exercise,
#     keep in mind a user can click on both ads, so the events are not mutually exclusive — use the addition rule.
def main():
    p_a = 12 / 100
    p_b = 17 / 100
    p_a_and_b = 3 / 100

    p_a_or_b = p_a + p_b - p_a_and_b


if __name__ == '__main__':
    main()
