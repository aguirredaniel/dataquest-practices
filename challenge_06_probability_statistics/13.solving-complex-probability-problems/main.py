# - A company that develops a time-tracking tool sells two kinds of subscription: basic and premium. When a new user
#  tries the product, there's a 0.2 probability the user buys the basic subscription and 0.15 he buys premium. Find:
#   - The probability that a new user doesn't buy a basic subscription (you'll need to use the P(E) = 1 - P(non-E)
#     formula). Assign your result to p_non_basic.
#   - The probability that a new user doesn't buy a premium subscription. Assign your result to p_non_premium.
#   - The probability that a user buys either basic or premium. Assign your result to p_subscription (assume buying
#     basic and buying premium are mutually exclusive).
#   - The probability that a new user doesn't buy a subscription. Assign your result to p_non_subscription.
def main():
    p_non_basic = 1 - 0.2
    p_non_premium = 1 - 0.15
    p_subscription = 0.2 + 0.15
    p_non_subscription = 1 - p_subscription

    print(p_subscription, p_non_subscription, sep='\n')


if __name__ == '__main__':
    main()
