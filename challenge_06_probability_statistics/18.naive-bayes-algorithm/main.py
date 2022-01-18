# - A new mobile message has been received: "URGENT!! You have one day left to claim your $873 prize." The following
#   probabilities are known:
#   - P(Spam)=0.5
#   - P(SpamC)=0.5
#   - P(New message)=0.5417
#   - P(NewMessage|Spam)=0.75
#   - P(NewMessage|SpamC)=0.3334
# - Classify this new message as spam or non-spam:
#   - Calculate P(Spam|New Message). Assign your answer to p_spam_given_new_message.
#   - Calculate P(SpamC|New Message). Assign your answer to p_non_spam_given_new_message.
#   - Classify the message by comparing the probability values. If the message is spam, then assign the string 'spam'
#     to the variable classification. Otherwise, assign the string 'non-spam'.
def main():
    p_spam = 0.5
    p_non_spam = 0.5
    p_new_message = 0.5417
    p_new_message_given_spam = 0.75
    p_new_message_given_non_spam = 0.3334

    p_spam_given_new_message = p_spam * p_new_message_given_spam / p_new_message

    p_non_spam_given_new_message = p_non_spam * p_new_message_given_non_spam / p_new_message

    classification = 'spam' if p_spam_given_new_message > p_non_spam_given_new_message else 'non-spam'

    print(p_spam_given_new_message, p_non_spam_given_new_message, classification, sep='\n')


if __name__ == '__main__':
    main()
