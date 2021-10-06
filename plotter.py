# 
# This file deals with all things plotting from 'temperature_data.csv' 
# 
# Josh Carlile, Hydroside Systems, 2021
# 

import matplotlib.pyplot as plt


# TODO: Somehow import data from csv

def plotSetup():
    plt.style.use('fivethirtyeight')

    plt.tight_layout()
    plt.show()

def updatePlot(x_data, y_data, fieldnames):
    ''' Provide y_data as a list of lists -- each a single dataset.
        x_data should be a list (probably of time)
        fieldnames should be a list "Therm 1", "Therm 2", ... '''

    plt.cla()

    for i in range(y_data):
        plt.plot(x_data, y_data[i], fieldnames[i])