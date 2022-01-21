import numpy as np
import matplotlib.pyplot as plt


def main():
    data = np.genfromtxt('weight_loss.csv', delimiter=',')
    weight_lost_a = data[1:, :1]
    weight_lost_b = data[1:, 1:]

    mean_group_a = np.mean(weight_lost_a)
    mean_group_b = np.mean(weight_lost_b)

    print(mean_group_a, mean_group_b, sep='\n')


if __name__ == '__main__':
    main()
