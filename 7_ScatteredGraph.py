import matplotlib.pyplot as plt
import numpy as np

# #day1
# x = np.array([2,4,6,8,10,20,25,30])
# y = np.array([30,10,20,50,40,35,100,15])

# plt.scatter(x,y, color='green')

# #day2
# x = np.array([2,4,6,8,10,20,25,30])
# y = np.array([39,17,29,89,45,55,76,19])

# #we can change all markers color in single plot
# colors = ['green','blue', 'black', 'red', 'cyan', 'pink', 'orange', 'yellow']
# plt.scatter(x,y, color=colors)
# #Instead of above colors we can also use color mapping
# colorMaps = np.array([5,10,20,30,40,50,60,70])
# plt.scatter(x,y, c=colorMaps, cmap='viridis')
# #To add color bar
# plt.colorbar()
# plt.show()

#Scatters alpha -> use to make the markers light

x = np.random.randint(50, size=10)
y = np.random.randint(50, size=10)
colors = np.random.randint(50, size=10)
sizes = 10*np.random.randint(10, size=10)

plt.scatter(x,y, c=colors, cmap='nipy_spectral', s=sizes, alpha=0.5)
plt.colorbar()
plt.show()