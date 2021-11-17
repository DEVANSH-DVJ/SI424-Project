import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def init():
    # Extract required data
    data_file = 'PS/population_Country.csv'
    data = pd.read_csv(data_file, sep=',').drop(columns='Unnamed: 0')
    data_cy = data.drop(
        columns=['Age', 'Female1', 'Male1',
                 'Total1', 'Total2', 'OpenInterval']).groupby(by=['Country', 'Year']).sum()

    # List of gender ratio for both countries
    ratio_cy = data_cy['Female2'] / data_cy['Male2']
    rls = [np.array(ratio_cy['ITA']), np.array(ratio_cy['AUS'])]
    return rls


def test1(ratios):
    # Reject H0 if mean is less than 1.0
    return ratios.mean() < 1.0


def test2(ratios):
    # Reject H0 if mean of min and max is less than 1.0
    return (ratios.min() + ratios.max()) / 2 < 1.0


def run(rls, K, N):
    outcomes1 = np.zeros((2, 2))
    outcomes2 = np.zeros((2, 2))

    for _ in range(N):
        # Generate subset with H0 as truth
        ratios = np.random.choice(rls[0], K, replace=False)
        # Perform tests
        res1 = test1(ratios)
        res2 = test2(ratios)
        # Save the test result
        if res1 == 0:
            outcomes1[0, 0] += 1  # Support H0
        else:
            outcomes1[0, 1] += 1  # Reject H0
        if res2 == 0:
            outcomes2[0, 0] += 1  # Support H0
        else:
            outcomes2[0, 1] += 1  # Reject H0

        # Generate subset with H1 as truth
        ratios = np.random.choice(rls[1], K, replace=False)
        # Perform tests
        res1 = test1(ratios)
        res2 = test2(ratios)
        # Save the test result
        if res1 == 0:
            outcomes1[1, 0] += 1  # Support H0
        else:
            outcomes1[1, 1] += 1  # Reject H0
        if res2 == 0:
            outcomes2[1, 0] += 1  # Support H0
        else:
            outcomes2[1, 1] += 1  # Reject H0

    # Return table of true vs predicted percentage for both tests
    return outcomes1 / (2*N), outcomes2 / (2*N)


if __name__ == '__main__':
    np.random.seed(0)
    rls = init()
    for N in [10, 100, 1000]:
        for K in range(1, 98, 10):
            t1, t2 = run(rls, K, N)
            print('N={}, K={}, t1=[{},{}], t2=[{},{}]'.format(N, K, *t1, *t2))
