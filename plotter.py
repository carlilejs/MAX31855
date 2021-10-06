# 
# This file deals with all things plotting from 'temperature_data.csv' 
# 
# Josh Carlile, Hydroside Systems, 2021
# 

import matplotlib.pyplot as plt

#def plotSetup():
plt.style.use('fivethirtyeight')



def updatePlot(x_data, y_data, fieldnames):
    ''' Provide y_data as a list of lists -- each a single dataset.
        x_data should be a list (probably of time)
        fieldnames should be a list "Therm 1", "Therm 2", ... '''

    plt.clf()

    for i in range( len(fieldnames) ):
        line = ax.plot(x_data, y_data)

    plt.show()

plt.tight_layout()
plt.show()

plotSetup()
updatePlot([1,2,3],[3,5,6],['First','Second','Third'])
