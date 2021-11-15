import pandas as pd

input_file = 'PS/population_Country.csv'
countries = ['AUS', 'GRC', 'ITA', 'UKR', 'USA']
columns = ['Year', 'Age', 'OpenInterval', 'Female1', 'Male1',
           'Total1', 'Female2', 'Male2', 'Total2', 'Country']

if __name__ == '__main__':
    data = pd.read_csv(input_file, sep=',')
    data = data.drop(columns='Unnamed: 0')
    data_us_year = data[data['Country'] == 'USA'].drop(
        columns=['Age', 'OpenInterval', 'Female1', 'Male1',
                 'Total1', 'Female2', 'Male2']).groupby(by='Year').sum()
    print(data_us_year)
    data_country_year = data.drop(
        columns=['Age', 'OpenInterval', 'Female1', 'Male1',
                 'Total1', 'Female2', 'Male2']).groupby(by=['Country', 'Year']).sum()
    print(data_country_year)
    exit(0)
