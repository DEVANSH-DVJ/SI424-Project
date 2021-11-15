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

    for i in range(len(countries)):
        country = countries[i]
        plt.scatter(population_ca['Total2'][country],
                    [i]*len(population_ca['Total2'][country]), label=country)
        print(len(population_ca['Total2'][country]), country)
    plt.grid()
    plt.legend()
    plt.show()
    for i in range(len(countries)):
        country = countries[i]
        (population_ca['Total2'][country] / population_ca['Total2'][country].sum()).plot()
    plt.show()

    exit(0)
