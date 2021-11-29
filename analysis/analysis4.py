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
    gls = [growth_cy_ITA, growth_cy_AUS]
    return gls


if __name__ == '__main__':
    # Initialize
    gls = init()

    # Plot ITA
    plt.clf()
    gls[0].plot()
    plt.ylabel('Population Growth Rate')
    plt.title('Population Growth Rate of Italy Vs Year')
    plt.grid()
    plt.savefig('plots/problem4/plot_ita.png')

    # Plot AUS
    plt.clf()
    gls[1].plot()
    plt.ylabel('Population Growth Rate')
    plt.title('Population Growth Rate of Australia Vs Year')
    plt.grid()
    plt.savefig('plots/problem4/plot_aus.png')
