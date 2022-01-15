# - An airline transports passengers using two types of planes: a Boeing 737 and an Airbus A320.
#   - The Boeing operates 73% of the flights. Out of these flights, 3% arrive at the destination with a delay.
#   - The Airbus operates the remaining 27% of the flights. Out of these flights, 8% arrive with a delay.
# - Convert the percentages above to probabilities:
#   - Assign the probability of flying with a Boeing to p_boeing (to better understand what this probability means,
#     imagine a passenger having bought a ticket with this airline — what's the probability that this passenger will be
#     assigned to fly to her destination with a Boeing?).
#   - Assign the probability of flying with an Airbus to p_airbus.
#   - Assign the probability of arriving at the destination with a delay given that the passenger flies with a Boeing
#     to p_delay_given_boeing.
#   - Assign the probability of arriving at the destination with a delay given that the passenger flies with an Airbus
#     to p_delay_given_airbus.
# - Calculate:
#   - The probability that a passenger will arrive at her destination with a delay. Assign your answer to p_delay. Check
#     the hint if you get stuck.
def main():
    p_boeing = 0.73
    p_airbus = 0.27
    p_delay_given_boeing = 0.03
    p_delay_given_airbus = 0.08

    p_delay = p_boeing * p_delay_given_boeing + p_airbus * p_delay_given_airbus


if __name__ == '__main__':
    main()
