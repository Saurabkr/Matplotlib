import matplotlib.pyplot as plt
import numpy as np

x = np.array([2,4,6,8,10])
y = np.array([30,10,20,50,40])

# plt.plot(x, y, marker='o')
# plt.plot(x, y, 'o:r')
# plt.show()

#marker:
# : -> dotted line
# - -> solid line
# -- -> dashed line
# -. -> dashed-dotted mix

#color reference
# r -> red
# b -> blue
# k -> black
# g -> green
# c -> cyan

#Marker size - ms
#Marker edge color - mec
#Marker face color - mfc

plt.plot(x,y, 'o-r',ms='5', mec='k', mfc='#008000') #we can also pass hex value of color
plt.show()