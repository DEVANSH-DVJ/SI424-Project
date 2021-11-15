import pandas as pd
import matplotlib.pyplot as plt

population_file = 'PS/population_Country.csv'
population_columns = ['Year', 'Age', 'OpenInterval', 'Female1', 'Male1',
                      'Total1', 'Female2', 'Male2', 'Total2', 'Country']
countries = ['AUS', 'GRC', 'ITA', 'UKR', 'USA']

if __name__ == '__main__':
    population = pd.read_csv(population_file, sep=',').drop(columns='Unnamed: 0')
    population_cy = population.drop(
        columns=['Age', 'Female1', 'Male1',
                 'Total1', 'Total2', 'OpenInterval']).groupby(by=['Country', 'Year']).sum()
    ratio_cy = population_cy['Female2'] / population_cy['Male2']
    for i in range(len(countries)):
        country = countries[i]
        plt.scatter(ratio_cy[country], [i]*len(ratio_cy[country]), label=country)
        print(len(ratio_cy[country]), country)
    plt.grid()
    plt.legend()
    plt.show()
    for i in range(len(countries)):
        country = countries[i]
        ratio_cy[country].plot()
    plt.show()

    exit(0)
