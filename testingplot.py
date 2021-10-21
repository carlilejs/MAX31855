import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 1])

for i in range(20):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(.5)

plt.show()