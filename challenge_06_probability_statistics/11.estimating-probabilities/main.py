# - We tossed a coin 300 times and got tails 162 times.
#   - Find the probability of getting heads. Assign your result to p_heads_1.
#   - Transform the probability in p_heads_1 to a percentage value. Assign the result to percentage_1.
# - In a different trial, we tossed a coin 5,000 times and got tails 2,450 times.
#   - Find the probability of getting heads. Assign your result to p_heads_2.
#   - Transform the probability in p_heads_2 to a percentage value. Assign the result to percentage_2.
def main():
    p_heads_1 = (300 - 162) / 300
    percentage_1 = p_heads_1 * 100

    p_heads_2 = (5000 - 2450) / 5000
    percentage_2 = p_heads_2 * 100

    print(percentage_1, percentage_2, sep='\n')


if __name__ == '__main__':
    main()
