# - A company offering a browser-based task manager tool intends to do some targeted advertising based on people's
#   browsers. The data they collected about their users is described in the table below:
# - Find:
#   - P(Premium | Chrome) — the probability that a randomly chosen user has a premium subscription, provided their
#     browser is Chrome. Assign your answer to p_premium_given_chrome.
#   - P(Basic | Safari) — the probability that a randomly chosen user has a basic subscription, provided their browser
#     is Safari. Assign your answer to p_basic_given_safari.
#   - P(Free | Firefox)} — the probability that a randomly chosen user has a free subscription, provided their browser
#     is Firefox. Assign your answer to p_free_given_firefox.
#   - Between a Chrome user and a Safari user, who is more likely to have a premium subscription? If you think a Chrome
#     user is the answer, then assign the string 'Chrome' to a variable named more_likely_premium, otherwise assign
#     'Safari'. To solve this exercise, you'll also need to calculate P(Premium | Safari).
def main():
    p_premium_given_chrome = 158 / 2762
    p_basic_given_safari = 274 / 1288
    p_free_given_firefox = 2103 / 2285
    p_premium_given_safari = 120 / 1288
    more_likely_premium = 'Chrome' if p_premium_given_chrome > p_premium_given_safari else 'Safari'

    print(p_premium_given_chrome, p_basic_given_safari, p_free_given_firefox, more_likely_premium, sep='\n')


if __name__ == '__main__':
    main()
