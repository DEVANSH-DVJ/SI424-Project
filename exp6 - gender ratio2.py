import pandas as pd
import matplotlib.pyplot as plt

mortality_file = 'PS/mortality_Country.csv'
mortality_columns = ['Year', 'Age', 'Female', 'Male', 'Total', 'OpenInterval', 'Country']
countries = ['AUS', 'GRC', 'ITA', 'UKR', 'USA']

if __name__ == '__main__':
    mortality = pd.read_csv(mortality_file, sep=',').drop(columns='Unnamed: 0')
    mortality_cy = mortality.drop(
        columns=['Age', 'Total', 'OpenInterval']).groupby(by=['Country', 'Year']).sum()
    ratio_cy = mortality_cy['Female'] / mortality_cy['Male']
    for country in countries:
        ratio_cy[country].plot.box()

        plt.show()
    exit(0)
