# -Calculate P(SpamC|w1, w2, w3, w4). Assign the answer to p_non_spam_given_w1_w2_w3_w4. Check the hint if you get stuck
# - Compare P(SpamC|w1, w2, w3, w4) with P(Spam|w1, w2, w3, w4) and classify the message "secret place secret secret"
#   — if the message is spam, then assign the string 'spam' to the variable classification. Otherwise, assign the string
#   'non-spam'.
def main():
    p_spam_given_w1_w2_w3_w4 = 64 / 4802

    p_non_spam = 2 / 4
    p_non_spam_given_w1_w2_w3_w4 = p_non_spam * 2 / 9 * 1 / 9 * 2 / 9 * 2 / 9

    classification = 'spam' if p_spam_given_w1_w2_w3_w4 > p_non_spam_given_w1_w2_w3_w4 else 'non-spam'

    print(p_non_spam, classification, sep='\n')


if __name__ == '__main__':
    main()
