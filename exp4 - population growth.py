import pandas as pd
import matplotlib.pyplot as plt

population_file = 'PS/population_Country.csv'
population_columns = ['Year', 'Age', 'OpenInterval', 'Female1', 'Male1',
                      'Total1', 'Female2', 'Male2', 'Total2', 'Country']
countries = ['AUS', 'GRC', 'ITA', 'UKR', 'USA']

if __name__ == '__main__':
    population = pd.read_csv(population_file, sep=',').drop(columns='Unnamed: 0')
    population_cy = population.drop(
        columns=['Age', 'OpenInterval', 'Female1', 'Male1',
                 'Total1', 'Female2', 'Male2']).groupby(by=['Country', 'Year']).sum()

    for country in countries:
        (population_cy['Total2'][country].diff()[1:] /
         population_cy['Total2'][country][1:] * 100).plot()
    plt.show()
    exit(0)
