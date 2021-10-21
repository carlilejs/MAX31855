# 
# This file deals with all things plotting from 'temperature_data.csv' 
# 
# Josh Carlile, Hydroside Systems, 2021
# 

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy

plot = plt.plot([], [])

def update_plot(plot, x_data, y_data):
    plot.set_xdata(numpy.append(plot.get_data(), x_data))
    plot.set_ydata(numpy.append(plot.get_ydata, y_data))
    plt.draw()
    plt.pause(0.01)


update_plot(plot, [1,2,3], [2,3,4])