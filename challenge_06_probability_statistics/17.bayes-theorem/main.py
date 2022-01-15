# - We can find the word "secret" in many spam emails. However, some emails are not spam even though they contain the
#   word "secret." Let's say we know the following probabilities:
#   - The probability of getting a spam email is 23.88%. That is P ( S p a m ) = 0.2388 .
#   - The probability of an email containing the word "secret" given that the email is spam is 48.02%. That is
#     P ( "secret" | S p a m ) = 0.4802 .
#   - The probability of an email containing the word "secret" given that the email is not spam is 12.84%. That is
#      P ( "secret" | S p a m C ) = 0.1284 .
# - Calculate:
#   - P(SpamC). Assign the result to p_non_spam.
#   - P(Spam ∩ "secret"). Assign the result to p_spam_and_secret.
#   - P(SpamC ∩ "secret"). Assign the result to p_non_spam_and_secret. P("secret"). Assign the result to p_secret.
def main():
    p_spam = 0.2388  # p(spam)
    p_secret_given_spam = 0.4802  # p(secret | spam)
    p_secret_given_non_spam = 0.1284  # p('secret' | not spam)

    p_non_spam = 1 - p_spam
    p_spam_and_secret = p_spam * p_secret_given_spam
    p_non_spam_and_secret = p_non_spam * p_secret_given_non_spam
    p_secret = p_spam * p_secret_given_spam + p_non_spam * p_secret_given_non_spam


if __name__ == '__main__':
    main()
