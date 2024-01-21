import matplotlib.pyplot as plt
import numpy as np

#plot1
x = np.array([2,4,6,8,10,20,25,30])
y = np.array([30,10,20,50,40,35,100,15])

plt.subplot(2,2,1) # 2-> row, 2-> column, 1-> 1st graph
plt.plot(x,y)
plt.title("Sale")
#plot2
x = np.array([2,4,6,8,10,20,25,30])
y = np.array([30,10,20,40,40,25,100,15])

plt.subplot(2,2,2) # 2-> row, 2-> column, 2-> 2st graph
plt.plot(x,y)
plt.title("Sale")
#plot3
x = np.array([2,4,6,8,10,20,25,30])
y = np.array([30,90,20,50,40,25,100,15])

plt.subplot(2,2,3) # 2-> row, 2-> column, 3-> 3st graph
plt.plot(x,y)
plt.title("Sale")
#plot4
x = np.array([2,4,6,8,10,20,25,30])
y = np.array([30,10,20,50,40,25,5,15])

plt.subplot(2,2,4) # 2-> row, 2-> column, 4-> 4st graph
plt.plot(x,y)
plt.title("Sale")

plt.suptitle("Shop Performance")
plt.show()

