# - On the last screen, our observed values were 10771 Females, and 21790 Males. Our expected values were 16280.5
#   Females and 16280.5 Males.
# - Compute the difference in number of observed Females vs number of expected Females using the updated technique.
#   Assign the result to female_diff.
# - Compute the difference in number of observed Males vs number of expected Males using the updated technique. Assign
#   the result to male_diff.
# - Add male_diff and female_diff together and assign to the variable gender_chisq.
def main():
    female_diff = (10771 - 16280.5) ** 2 / 16280.5
    male_diff = (21790 - 16280.5) ** 2 / 16280.5
    gender_chisq = female_diff + male_diff
    print(female_diff, male_diff, gender_chisq,  sep='\n')


if __name__ == '__main__':
    main()
