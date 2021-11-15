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
    increase_cy = population_cy.diff().dropna()
    for country in countries:
        # population_cy['Total2'][country].plot()
        (population_cy['Total2'][country].diff().dropna() / population_cy['Total2'][country]).plot()
        plt.show()
    exit(0)
