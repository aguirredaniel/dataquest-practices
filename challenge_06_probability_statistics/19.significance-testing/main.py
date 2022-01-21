import numpy as np
import matplotlib.pyplot as plt


def main():
    data = np.genfromtxt('weight_loss.csv', delimiter=',')
    weight_lost_a = data[1:, :1]
    weight_lost_b = data[1:, 1:]

    mean_group_a = np.mean(weight_lost_a)
    mean_group_b = np.mean(weight_lost_b)

    mean_difference = mean_group_b - mean_group_a

    all_values = data.flatten()
    mean_differences = []

    for _ in range(1000):
        group_a = []
        group_b = []
        for weight_lost in all_values:
            random = np.random.rand(1, 1)
            if random >= 0.5:
                group_a.append(weight_lost)
            else:
                group_b.append(weight_lost)

        iteration_mean_difference = np.mean(group_b) - np.mean(group_a)
        mean_differences.append(iteration_mean_difference)

    plt.hist(mean_differences)
    plt.show()


if __name__ == '__main__':
    main()
