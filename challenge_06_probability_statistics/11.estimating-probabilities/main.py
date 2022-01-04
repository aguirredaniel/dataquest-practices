# - An insurance company conducted a study with 200 individuals, and found that:
#   - 87 individuals opted for at least a life insurance policy.
#   - 40 individuals opted for at least life and car insurance policies.
#   - 63 individuals opted for at least a house insurance policy.
#   - 160 individuals opted for at least one type of insurance policy.
# - We can't predict people's choices with certainty, so an individual choosing to buy an insurance policy is a random
#   experiment. 200 individuals were part of the study, so you can consider the random experiment was performed 200
#   times. Find:
#   - P(L): The probability that a new customer opts for at least a life insurance. Assign your answer to a variable
#     named p_l.
#   - P(L and C): The probability that an individual opts for at least a life and a car insurance policy. Assign your
#     answer to a variable named p_l_and_c.
#   - P(H): The probability that an individual opts for at least a house insurance policy. Assign your answer to a
#     variable named p_h.
#   -P(NO): The probability that an individual opts for no insurance at all. Assign your answer to a variable named
#    p_no.
def main():
    p_l = 87 / 200
    p_l_and_c = 40 / 200
    p_h = 63 / 200
    p_no = (200 - 160) / 200
    print(p_l, p_l_and_c, p_h, p_no, sep='\n')


if __name__ == '__main__':
    main()
