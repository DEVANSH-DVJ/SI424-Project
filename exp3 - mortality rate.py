import pandas as pd
import matplotlib.pyplot as plt

mortality_file = 'PS/mortality_Country.csv'
mortality_columns = ['Year', 'Age', 'Female', 'Male', 'Total', 'OpenInterval', 'Country']
population_file = 'PS/population_Country.csv'
population_columns = ['Year', 'Age', 'OpenInterval', 'Female1', 'Male1',
                      'Total1', 'Female2', 'Male2', 'Total2', 'Country']
countries = ['AUS', 'GRC', 'ITA', 'UKR', 'USA']

if __name__ == '__main__':
    mortality = pd.read_csv(mortality_file, sep=',').drop(columns='Unnamed: 0')
    mortality_cy = mortality.drop(
        columns=['Age', 'Female', 'Male', 'OpenInterval']).groupby(by=['Country', 'Year']).sum()
    print(mortality_cy)
    population = pd.read_csv(population_file, sep=',').drop(columns='Unnamed: 0')
    population_cy = population.drop(
        columns=['Age', 'OpenInterval', 'Female1', 'Male1',
                 'Total1', 'Female2', 'Male2']).groupby(by=['Country', 'Year']).sum()
    print(population_cy)
    rate_cy = mortality_cy['Total'] / population_cy['Total2'] * 100

    for i in range(len(countries)):
        country = countries[i]
        plt.scatter(population_cy['Total2'][country],
                    [i]*len(population_cy['Total2'][country]), label=country)
        print(len(population_cy['Total2'][country]), country)
    plt.grid()
    plt.legend()
    plt.show()
    for i in range(len(countries)):
        country = countries[i]
        # mortality_cy['Total'][country].plot()
        # plt.show()
        # population_cy['Total2'][country].plot()
        # plt.show()
        # rate_cy[country].plot()
        # plt.show()

    exit(0)
