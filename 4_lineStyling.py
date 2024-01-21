import matplotlib.pyplot as plt
import numpy as np

x = np.array([2,4,6,8,10])
y = np.array([30,10,20,50,40])

plt.plot(x, y, linestyle='-.', color='b', linewidth='10')
plt.show()