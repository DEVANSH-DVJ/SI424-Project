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

    # Population growth rate
    growth_cy_ITA = (population_cy['Total2']['ITA'].diff()[1:] /
                     population_cy['Total2']['ITA'][1:] * 100)
    return growth_cy_ITA


def estimator(ratelist):
    # The estimate of mu is the mean; of sigma is the standard deviation
    return (ratelist.mean(), ratelist.std(ddof=0))


def run(md, K, N):
    mu_estimates = np.zeros((N, 1))
    sigma_estimates = np.zeros((N, 1))

    for i in range(N):
        # Generate growth rate from the underlying true population data
        ratelist = np.random.choice(md, K, replace=False)
        # Save the estimated values
        estimate = estimator(ratelist)
        mu_estimates[i] = estimate[0]
        sigma_estimates[i] = estimate[1]

    # Return average estimated value and std. deviation of estimated values
    return ((mu_estimates.mean(), mu_estimates.std()),
            (sigma_estimates.mean(), sigma_estimates.std()))


if __name__ == '__main__':
    # Set seed
    np.random.seed(0)

    # Initialize
    aps = init()

    for N in [10, 100, 1000, 10000]:
        mu_avgs = []
        mu_stds = []
        sigma_avgs = []
        sigma_stds = []

        for K in range(10, 146, 1):
            # Run the experiment for given K, N
            est_info = run(aps, K, N)
            print('N={}, K={}, mu={}, sigma={}'.format(N, K, est_info[0], est_info[1]))

            mu_avgs.append(est_info[0][0])
            mu_stds.append(est_info[0][1])

            sigma_avgs.append(est_info[1][0])
            sigma_stds.append(est_info[1][1])

        # For Estimate of Mu
        # Plot Avg
        plt.clf()
        plt.plot(range(10, 146, 1), mu_avgs)
        plt.xlabel('K')
        plt.ylim((0.46, 0.64))
        plt.ylabel('Average estimated value of mean')
        plt.title('Performed {} experiments for each K'.format(N))
        plt.grid()
        plt.savefig('plots/problem1/Mean/avgs_{}.png'.format(N))

        # Plot Std. dev.
        plt.clf()
        plt.plot(range(10, 146, 1), mu_stds)
        plt.xlabel('K')
        plt.ylim((-0.01, 0.24))
        plt.ylabel('Std. deviation of estimated value of mean')
        plt.title('Performed {} experiments for each K'.format(N))
        plt.grid()
        plt.savefig('plots/problem1/Mean/stds_{}.png'.format(N))

        # For Estimate of Sigma
        # Plot Avg
        plt.clf()
        plt.plot(range(10, 146, 1), sigma_avgs)
        plt.xlabel('K')
        plt.ylim((0.34, 0.71))
        plt.ylabel('Average estimated value of sigma')
        plt.title('Performed {} experiments for each K'.format(N))
        plt.grid()
        plt.savefig('plots/problem1/Std/avgs_{}.png'.format(N))

        # Plot Std. dev.
        plt.clf()
        plt.plot(range(10, 146, 1), sigma_stds)
        plt.xlabel('K')
        plt.ylim((-0.02, 0.46))
        plt.ylabel('Std. deviation of estimated value of sigma')
        plt.title('Performed {} experiments for each K'.format(N))
        plt.grid()
        plt.savefig('plots/problem1/Std/stds_{}.png'.format(N))
