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
    rls = [ratio_cy['ITA'], ratio_cy['AUS']]
    return rls


if __name__ == '__main__':
    # Initialize
    gls = init()

    # Plot ITA
    plt.clf()
    gls[0].plot()
    plt.ylabel('Gender Ratio')
    plt.title('Gender Ratio of Italy Vs Year')
    plt.grid()
    plt.savefig('plots/problem3/plot_ita.png')

    # Plot AUS
    plt.clf()
    gls[1].plot()
    plt.ylabel('Gender Ratio')
    plt.title('Gender Ratio of Australia Vs Year')
    plt.grid()
    plt.savefig('plots/problem3/plot_aus.png')
