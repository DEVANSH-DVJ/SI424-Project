import pandas as pd
import matplotlib.pyplot as plt

population_file = 'PS/population_Country.csv'
population_columns = ['Year', 'Age', 'OpenInterval', 'Female1', 'Male1',
                      'Total1', 'Female2', 'Male2', 'Total2', 'Country']
countries = ['AUS', 'GRC', 'ITA', 'UKR', 'USA']

if __name__ == '__main__':
    population = pd.read_csv(population_file, sep=',').drop(columns='Unnamed: 0')
    population_ca = population.drop(
        columns=['OpenInterval', 'Female1', 'Male1',
                 'Total1', 'Female2', 'Male2']).groupby(['Country', 'Age']).sum()
    # print(population_ca)
    for country in countries:
        population_ca['Total2'][country].plot()
        plt.show()
    exit(0)
