import csv
from County import County
#Loading counties in and storing in dictionary
#doesn't store any information about the people themselves (saves ram)
county_dict = {}
counties = ['ALA','BAK', 'BAY', 'BRA', 'BRE', 'BRO', 'CAL', 'CHA', 'CIT', 'CLA', 
            'CLL', 'CLM', 'DAD', 'DES', 'DIX', 'DUV', 'ESC', 'FLA', 'FRA', 'GAD',
           'GIL', 'GLA', 'GUL', 'HAM', 'HAR', 'HEN', 'HER', 'HIG', 'HIL', 'HOL',
           'IND', 'JAC', 'JEF', 'LAF', 'LAK', 'LEE', 'LEO', 'LEV', 'LIB', 'MAD',
           'MAN', 'MRN', 'MRT', 'MON', 'NAS', 'OKA', 'OKE', 'ORA', 'OSC', 'PAL', 'PAS',
           'PIN', 'POL', 'PUT', 'SAN', 'SAR', 'SEM', 'STJ', 'STL', 'SUM', 'SUW', 'TAY',
           'UNI', 'VOL', 'WAK', 'WAL', 'WAS']
for county_name in counties:
    temp_county = County(county_name)
    temp_county.load_data()
    temp_county.process_data()
    temp_county.create_file()
    county_dict[county_name] = temp_county

#when search is input just call it on the county object here

#First search function, can pass directly to
#Hashmap based
def search_regular(name, address, county):
    if not bool(county_dict[county].people_dict):
        county_dict[county].store_people()
    county_dict[county].search_people_regular(name, address)


#Tree based
def search_sorted(name, address, county):
    if not bool(county_dict[county].people_dict):
        county_dict[county].store_people()
    county_dict[county].search_people_sorted(name, address)

#function to read data from the statistics file
def read_stats(county_code):
    with open("statistics.txt", "r") as statistics_file:
            reader = csv.reader(statistics_file, dialect="excel-tab")
            for row in reader:
                if row[0] == county_code:
                    for i in row:
                        print(i)
