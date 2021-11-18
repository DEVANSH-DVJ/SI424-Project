import pandas as pd
import matplotlib.pyplot as plt

mortality_file = 'PS/mortality_Country.csv'
mortality_columns = ['Year', 'Age', 'Female', 'Male', 'Total', 'OpenInterval', 'Country']
countries = ['AUS', 'GRC', 'ITA', 'UKR', 'USA']

if __name__ == '__main__':
    mortality = pd.read_csv(mortality_file, sep=',').drop(columns='Unnamed: 0')
    mortality_ca = mortality.drop(
        columns=['Female', 'Male', 'OpenInterval']).groupby(['Country', 'Year', 'Age']).sum()

    for i in range(2000, 2016):
        print(i)
        (mortality_ca['Total']['GRC'][i] / mortality_ca['Total']['GRC'][i].sum()).plot()
        plt.show()

    exit(0)
