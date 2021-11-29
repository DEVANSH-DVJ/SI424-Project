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


if __name__ == '__main__':
    # Initialize
    growth_cy_ITA = init()

    # Plot
    plt.clf()
    growth_cy_ITA.plot()
    plt.ylabel('Population Growth Rate')
    plt.title('Population Growth Rate of Italy Vs Year')
    plt.grid()
    plt.savefig('plots/problem1/plot.png')

    # Histogram
    plt.clf()
    growth_cy_ITA.plot.hist(bins=20)
    plt.xlabel('Population Growth Rate')
    plt.title('20 bin Histogram Population Growth Rate of Italy')
    plt.grid()
    plt.savefig('plots/problem1/hist.png')
