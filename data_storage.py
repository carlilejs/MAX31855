import json
import matplotlib.pyplot as plt
import csv


def setupPlot():
    plt.style.use('fivethirtyeight')

    for _ in range(0,7):
        plt.plot(0,0)

    plt.tight_layout()
    plt.show()

def animatePlot():
    return

setupPlot()


