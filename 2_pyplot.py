import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,4,5,6])
y = np.array([4,7,9,10,15])

# plt.plot(x, y, 'o') #In this graph we get points instead of line
# plt.plot(x, y)

# plt.show()

# we can also pass only one axis inside the plot function
plt.plot(y)
plt.show()
