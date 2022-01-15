# - An airline transports passengers using two types of planes: a Boeing 737 and an Airbus A320.
#   - The Boeing operates 73% of the flights. Out of these flights, 3% arrive at the destination with a delay.
#   - The Airbus operates the remaining 27% of the flights. Out of these flights, 8% arrive with a delay.
#   - Use Bayes' theorem to find P(Airbus|Delay). Assign your answer to p_airbus_delay. Don't forget you can check the
#     hint if you get stuck.
def main():
    p_spam = 0.2388
    p_secret_given_spam = 0.4802
    p_secret_given_non_spam = 0.1284
    p_non_span = 1 - p_spam
    p_secret = p_spam * p_secret_given_spam + p_non_span * p_secret_given_non_spam

    p_spam_given_secret = (p_spam * p_secret_given_spam) / p_secret
    prior = p_spam
    posterior = p_spam_given_secret
    ratio = posterior / prior

    print(p_spam_given_secret, prior, posterior, ratio, sep='\n')


if __name__ == '__main__':
    main()
