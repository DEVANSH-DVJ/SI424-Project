import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def init():
    # Extract required data
    data_file = 'PS/population_Country.csv'
    data = pd.read_csv(data_file, sep=',').drop(columns='Unnamed: 0')
    population_cy = data.drop(
        columns=['Age', 'OpenInterval', 'Female1', 'Male1',
                 'Total1', 'Female2', 'Male2']).groupby(by=['Country', 'Year']).sum()

    # List of population growth rate for both countries
    growth_cy_ITA = (population_cy['Total2']['ITA'].diff()[1:] /
                     population_cy['Total2']['ITA'][1:] * 100)
    growth_cy_AUS = (population_cy['Total2']['AUS'].diff()[1:] /
                     population_cy['Total2']['AUS'][1:] * 100)
    gls = [np.array(growth_cy_ITA), np.array(growth_cy_AUS)]
    return gls


def test(ratios):
    # Reject H0 if mean is greater than 1.2
    return ratios.mean() > 1.2


def run(gls, K, N):
    outcomes = np.zeros((2, 2))

    for _ in range(N):
        # Generate subset with H0 as truth
        ratios = np.random.choice(gls[0], K, replace=False)
        # Perform tests
        res = test(ratios)
        # Save the test result
        if res == 0:
            outcomes[0, 0] += 1  # Support H0
        else:
            outcomes[0, 1] += 1  # Reject H0

        # Generate subset with H as truth
        ratios = np.random.choice(gls[1], K, replace=False)
        # Perform tests
        res = test(ratios)
        # Save the test result
        if res == 0:
            outcomes[1, 0] += 1  # Support H0
        else:
            outcomes[1, 1] += 1  # Reject H0

    # Return table of true vs predicted percentage for the test
    return outcomes / (2*N)


if __name__ == '__main__':
    # Set seed
    np.random.seed(0)

    # Initialize
    gls = init()

    for N in [10, 100, 1000, 10000]:
        type1 = []
        type2 = []

        for K in range(1, 98, 1):
            # Run the experiment for given K, N
            t = run(gls, K, N)
            print('N={}, K={}, t=[{},{}]'.format(N, K, *t))

            type1.append(t[0, 1] * 2)
            type2.append(t[1, 0] * 2)

        # Plot Type I error
        plt.clf()
        plt.plot(range(1, 98, 1), type1)
        plt.xlabel('K')
        plt.ylim((-0.01, 0.11))
        plt.ylabel('Average Type I error')
        plt.title('Performed {} experiments for each K'.format(N))
        plt.grid()
        plt.savefig('./plots/problem4/type1_{}.png'.format(N))

        # Plot Type I error
        plt.clf()
        plt.plot(range(1, 98, 1), type2)
        plt.xlabel('K')
        plt.ylim((-0.01, 0.41))
        plt.ylabel('Average Type II error')
        plt.title('Performed {} experiments for each K'.format(N))
        plt.grid()
        plt.savefig('./plots/problem4/type2_{}.png'.format(N))
