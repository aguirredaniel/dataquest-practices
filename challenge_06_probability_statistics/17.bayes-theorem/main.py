# - An airline transports passengers using three types of planes: a Boeing 737, an Airbus A320, and an ERJ 145.
#   - The Boeing operates 62% of the flights. Out of these flights, 6% arrive at the destination with a delay.
#   - The Airbus operates 35% of the flights. Out of these flights, 9% arrive with a delay.
#   - The ERJ operates the remaining 3% of the flights. Out of these flights, 1% arrive with a delay.
# - Calculate the probability of delay and assign your result to p_delay. See the hint if you get stuck.
def main():
    p_boeing = 0.62
    p_airbus = 0.35
    p_erj = 0.03
    p_delay_boeing = 0.06
    p_delay_airbus = 0.09
    p_delay_erj = 0.01

    p_delay = p_boeing * p_delay_boeing + p_airbus * p_delay_airbus + p_erj * p_delay_erj
    print(p_delay)


if __name__ == '__main__':
    main()
