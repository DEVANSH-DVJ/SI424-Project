import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def init():
    # Extract required data
    data_file = 'PS/mortality_Country.csv'
    data = pd.read_csv(data_file, sep=',').drop(columns='Unnamed: 0')
    data_cya = data.drop(
        columns=['Female', 'Male', 'OpenInterval']).groupby(['Country', 'Year', 'Age']).sum()

    # Probability of each age interval
    aps = (data_cya['Total']['GRC'][2005] / data_cya['Total']['GRC'][2005].sum())
    return aps


def estimator(agelist):
    # The estimate is the mean
    return agelist.mean() / 110


def run(aps, K, N):
    estimates = np.zeros((N, 1))

    for i in range(N):
        # Generate age in [0, 111) with the above computed probabilities
        agelist = np.random.choice(111, K, p=aps)
        # Save the estimated value
        estimates[i] = estimator(agelist)

    # Return average estimated value and std. deviation of estimated value
    return estimates.mean(), estimates.std(ddof=1)


if __name__ == '__main__':
    # Set seed
    np.random.seed(0)

    # Initialize
    aps = init()

    for N in [10, 100, 1000]:
        avgs = []
        stds = []

        for K in range(10, 5000, 10):
            # Run the experiment for given K, N
            est_info = run(aps, K, N)
            print('N={}, K={}, p={}'.format(N, K, est_info))

            avgs.append(est_info[0])
            stds.append(est_info[1])

        # Plot Avg
        plt.clf()
        plt.plot(range(10, 5000, 10), avgs)
        plt.xlabel('K')
        plt.ylim((0.674, 0.701))
        plt.ylabel('Average estimated value of p')
        plt.title('Performed {} experiments for each K'.format(N))
        plt.grid()
        plt.savefig('plots/problem2/avgs_{}.png'.format(N))

        # Plot Std. dev.
        plt.clf()
        plt.plot(range(10, 5000, 10), stds)
        plt.xlabel('K')
        plt.ylim((-0.002, 0.048))
        plt.ylabel('Std. deviation of estimated value of p')
        plt.title('Performed {} experiments for each K'.format(N))
        plt.grid()
        plt.savefig('plots/problem2/stds_{}.png'.format(N))
