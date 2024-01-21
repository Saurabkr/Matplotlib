import matplotlib.pyplot as plt
import numpy as np

x = np.array([2,4,6,8,10,20,25,30])
y = np.array([30,10,20,50,40,25,100,15])

#Font of label and title 
fontLable = {'family':'ariel', 'color':"red", 'size':'10'}
fontTitle = {'family':'serif', 'color':"red", 'size':'15'}

plt.plot(x, y)
#Set label and title of the graph
plt.xlabel("KM", fontdict=fontLable)
plt.ylabel("Calories",fontdict=fontLable)
#set location of title or label using loc
plt.title("Calorie burn per KM",fontdict=fontTitle, loc='left')
#Set grid and it's line property
plt.grid(axis='x', linewidth='0.7', linestyle='-.', color='green')
plt.show()

