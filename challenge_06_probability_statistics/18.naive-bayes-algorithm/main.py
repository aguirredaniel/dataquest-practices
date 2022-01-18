# - Calculate P(SpamC) and assign the answer to p_non_spam.
# - Calculate P("secret"|SpamC) and assign the answer to p_secret_given_non_spam.
# - Calculate P(SpamC|"secret") and assign the answer to p_non_spam_given_secret.
# - Compare P(SpamC|"secret") with P(Spam|"secret") and classify the message "secret" — if the message is spam, then
#   assign the string 'spam' to the variable classification, otherwise assign the string 'non-spam'.
def main():
    p_spam_given_secret = 8 / 21
    p_spam = 2 / 3
    p_non_spam = 1 - p_spam
    p_secret_given_non_spam = 1 / 4
    p_non_spam_given_secret = p_non_spam * p_secret_given_non_spam
    classification = 'spam' if p_spam_given_secret > p_non_spam_given_secret else 'non-spam'

    print(p_non_spam, p_secret_given_non_spam, p_non_spam_given_secret, classification, sep='\n')


if __name__ == '__main__':
    main()
