# - An airline transports passengers using two types of planes: a Boeing 737 and an Airbus A320.
#   - The Boeing operates 73% of the flights. Out of these flights, 3% arrive at the destination with a delay.
#   - The Airbus operates the remaining 27% of the flights. Out of these flights, 8% arrive with a delay.
#   - Use Bayes' theorem to find P(Airbus|Delay). Assign your answer to p_airbus_delay. Don't forget you can check the
#     hint if you get stuck.
def main():
    p_boeing = 0.73
    p_airbus = 0.27
    p_delay_given_boeing = 0.03
    p_delay_given_airbus = 0.08

    p_delay = p_boeing * p_delay_given_boeing + p_airbus * p_delay_given_airbus
    p_airbus_delay = (p_airbus * p_delay_given_airbus) / p_delay

    print(p_delay, p_airbus_delay, sep='\n')


if __name__ == '__main__':
    main()
