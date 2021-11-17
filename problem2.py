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
    return agelist.mean()


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
    np.random.seed(0)
    md = init()
    for N in [10, 100, 1000]:
        for K in [1, 5, 10, 50, 100, 1000, 10000]:
            print('N={}, K={}, p={}'.format(N, K, run(md, K, N)))
