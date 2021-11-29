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


if __name__ == '__main__':
    # Initialize
    aps = init()

    # Plot
    plt.clf()
    plt.scatter(range(111), aps)
    plt.xlabel('Age of death')
    plt.ylabel('Probability')
    plt.title('Probability distribution of Age of death in Greece in 2005')
    plt.grid()
    plt.savefig('plots/problem2/plot.png')
