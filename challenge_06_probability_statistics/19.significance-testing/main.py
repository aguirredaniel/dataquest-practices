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
    np.random.seed(1)
    sampling_size = 1000
    for _ in range(sampling_size):
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

    sampling_distribution = {}
    for md in mean_differences:
        val = sampling_distribution.get(md, 0)
        sampling_distribution[md] = val + 1

    frequencies = [sampling for sampling in sampling_distribution if sampling >= mean_difference]

    p_value = np.sum(frequencies) / sampling_size

    print(p_value)


if __name__ == '__main__':
    main()