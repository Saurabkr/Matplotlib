import matplotlib.pyplot as plt
import numpy as np

x = np.array([10,20,35,30,5])
pieColors = ['b','cyan','pink','green', 'yellow']
pieLabels = ['Maruti','Alto','Scorpio','BMW', 'Jaguar']
pieExplode = [0,0,0.3,0,0]

plt.pie(x, colors=pieColors, labels=pieLabels, explode=pieExplode, shadow=True)
plt.legend(title='Cars')
plt.show()