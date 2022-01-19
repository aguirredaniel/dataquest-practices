# -Calculate P(SpamC|"secret code to unlock the money"). Assign your answer to p_non_spam_given_message.
# - Print p_spam_given_message and p_non_spam_given_message. Why do you think we got these values? We'll discuss more
#   about this in the next screen.
def main():
    p_spam = 2 / 4
    p_secret_given_spam = (4 + 1) / (7 + 9)
    p_the_given_spam = 1 / (7 + 9)
    p_money_given_spam = (2 + 1) / (7 + 9)
    p_spam_given_message = (p_spam * p_secret_given_spam *
                            p_the_given_spam * p_money_given_spam)

    p_non_spam = 1 - p_spam
    p_secret_given_non_spam = (2 + 1) / (9 + 9)
    p_the_given_non_spam = (1 + 1) / (9 + 9)
    p_money_given_non_spam = 1 / (9 + 9)

    p_non_spam_given_message = p_non_spam * p_secret_given_non_spam * p_the_given_non_spam * p_money_given_non_spam
    classification = 'spam' if p_spam_given_message > p_non_spam_given_message else 'non-spam'
    print(p_spam_given_message, p_non_spam_given_message, classification, sep='\n')


if __name__ == '__main__':
    main()
