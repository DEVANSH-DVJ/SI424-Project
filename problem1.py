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
    return (ratelist.mean(), ratelist.std())

def run(md, K, N):
    MeanEstimates = np.zeros((N, 1))
    StdEstimates = np.zeros((N, 1))

    for i in range(N):
        # Generate growth rate from the underlying true population data
        ratelist = np.random.choice(md, K, replace = False)

        # Save the estimated values
        estimate = estimator(ratelist)
        MeanEstimates[i] = estimate[0]
        StdEstimates[i] = estimate[1]

    return [[MeanEstimates.mean(), MeanEstimates.std()], [StdEstimates.mean(), StdEstimates.std()]]


if __name__ == '__main__':
    # Set seed
    np.random.seed(0)

    # Initialize
    aps = init()

    for N in [10, 100, 1000]:
        avgs1 = []
        stds1 = []
        avgs2 = []
        stds2 = []

        for K in range(20, 141, 1):
            # Run the experiment for given K, N
            est_info = run(aps, K, N)
            print('N={}, K={}, p={}'.format(N, K, est_info))

            avgs1.append(est_info[0][0])
            stds1.append(est_info[0][1])

            avgs2.append(est_info[1][0])
            stds2.append(est_info[1][1])


        # For Estimate of Mu
        # Plot Avg
        plt.clf()
        plt.plot(range(20, 141, 1), avgs1)
        plt.xlabel('K')
        plt.ylim((0.45, 0.70))
        plt.ylabel('Average estimated value of mean')
        plt.title('Performed {} experiments for each K'.format(N))
        plt.grid()
        plt.savefig('plots/problem1/Mean/avgs_{}.png'.format(N))

        # Plot Std. dev.
        plt.clf()
        plt.plot(range(20, 141, 1), stds1)
        plt.xlabel('K')
        plt.ylim((-0.05, 0.55))
        plt.ylabel('Std. deviation of estimated value of mean')
        plt.title('Performed {} experiments for each K'.format(N))
        plt.grid()
        plt.savefig('plots/problem1/Mean/stds_{}.png'.format(N))


        # For Estimate of Sigma
        # Plot Avg
        plt.clf()
        plt.plot(range(20, 141, 1), avgs2)
        plt.xlabel('K')
        plt.ylim((0.2, 0.65))
        plt.ylabel('Average estimated value of sigma')
        plt.title('Performed {} experiments for each K'.format(N))
        plt.grid()
        plt.savefig('plots/problem1/Std/avgs_{}.png'.format(N))

        # Plot Std. dev.
        plt.clf()
        plt.plot(range(20, 141, 1), stds2)
        plt.xlabel('K')
        plt.ylim((-0.05, 0.55))
        plt.ylabel('Std. deviation of estimated value of sigma')
        plt.title('Performed {} experiments for each K'.format(N))
        plt.grid()
        plt.savefig('plots/problem1/Std/stds_{}.png'.format(N))
