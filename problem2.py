import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def init():
    data_file = 'PS/mortality_Country.csv'
    data = pd.read_csv(data_file, sep=',').drop(columns='Unnamed: 0')
    data_cya = data.drop(
        columns=['Female', 'Male', 'OpenInterval']).groupby(['Country', 'Year', 'Age']).sum()
    data_cdf = (data_cya['Total']['GRC'][2005] / data_cya['Total']['GRC'][2005].sum()).cumsum()

    md = np.zeros((111, 2))
    for i in range(110):
        md[i, 1] = data_cdf[i]
        md[i+1, 0] = data_cdf[i]
    md[110, 1] = 1.0

    return md


def estimator(md, K):
    uni = np.random.rand(K, 1)
    agelist = np.argmax((md[:, 0] <= uni) & (md[:, 1] > uni), axis=1)
    return agelist.mean()


def run(md, K, N):
    estimates = np.zeros((N, 1))
    for i in range(N):
        estimates[i] = estimator(md, K)
    return estimates.mean(), estimates.std(ddof=1)


if __name__ == '__main__':
    np.random.seed(0)
    md = init()
    for N in [10, 100, 1000]:
        for K in [1, 5, 10, 50, 100, 1000, 10000]:
            print('N={}, K={}, p={}'.format(N, K, run(md, K, N)))
