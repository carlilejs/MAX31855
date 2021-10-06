# 
# This file is for handling all reading from and writing to the 'temperature_data.csv' file.
# The file has been created before running this file, so there's no setup. 
# Josh Carlile, Hydroside Systems, 2021
# 

import csv

# NOTE: Complete
def read_newest_row():
    ''' Return list of values on the final row of temp_data.csv (including date)
        Used for plotting current values. '''
    with open('temp_data.csv') as file:
        # Convert DictReader to list so I can use pop()
        data_list = list(csv.DictReader(file))
        data = []

        # Data list is an array of dictionaries.
        # I'm iterating through all keys on the last row.
        last_row = data_list.pop()

        for key in last_row:
            data.append( last_row[key] )

        return data


# NOTE: Complete
def read_column(key):
    ''' Grab all data from a certain column off the excel spreadsheet.
        Used for plotting certain value over time. '''
    with open('temp_data.csv') as file:
        # Convert DictReader to list so I can index
        data_list = list(csv.DictReader(file))
        data = []

        # Iterate through all rows
        for row in data_list:
            term = 0    # Store current value

            # Error handling in case key isn't valid.
            try:
                term = row[key]
            except KeyError:
                print(f'Key \'{key}\' not valid.')
                return []
            else:
                data.append(term)

        return data

def write_next_row(data=[]):
    ''' Append a row of data to temp_data.csv  '''
    with open('temp_data.csv') as file:
        reader = csv.DictReader(file)
        # Need to use DictWriter to avoid stringification of numbers
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)

        formatted_data = {}

        for i in range(len(data)):
            try:
                formatted_data[reader.fieldnames[i]] = data[i]
            except:
                print('Error pushing data')
                raise
            else:
                writer.writerow(formatted_data)

# print( read_column('Therm 3') )
# print( 'Therm 2: ', read_newest(key = 'Therm 2') )
print( write_next_row([16,54,34,23,12]) )

# data = pd.read_csv('data.csv')
# x = data['x_value']
# y1 = data['total_1']
# y2 = data['total_2']