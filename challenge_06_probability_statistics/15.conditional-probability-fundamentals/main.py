# - Two fair six-sided dice are simultaneously rolled, and the two numbers they show are added together. The diagram
#   below shows all the possible results that we can get from adding the two numbers together.
# - Find P(A|B), where A is the event where the sum is an even number, and B is the event that the sum is less than
#   eight.
#   - Find card(B). Assign your answer to card_b.
#   - Note that you'll have to treat identical sums differently if they come from different die numbers. On the diagram
#     above, we see that we have three sums of 4, but they all come from different die outcomes: (3, 1), (2,2), and (1, 3), where the first number describes the outcome of the first die throw, and the second number the outcome of the second die throw.
#   - Find card(A ∩ B). Assign your answer to card_a_and_b.
#   - Calculate P(A|B). Assign your answer to p_a_given_b.
def main():
    card_b = 21
    card_a_and_b = 9
    p_a_given_b = card_a_and_b / card_b
    print(p_a_given_b, sep='\n')


if __name__ == '__main__':
    main()
