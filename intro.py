import matplotlib 
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)

x = np.array([0,10])
y = np.array([0,250])

plt.plot(x, y)
plt.show()


