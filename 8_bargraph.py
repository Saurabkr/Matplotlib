import matplotlib.pyplot as plt
import numpy as np

x = np.array(['Household', 'Fruits', 'Traveling', 'Cloth'])
labelX = plt.xlabel("Items")
y = np.array([2000,1000,4000,3000])
labelY = plt.ylabel("Expenses(Rs)") 

# plt.title("Monthly Expenditure")
# #Vertical bar graph
plt.bar(x,y,width=0.3, color="green")
# #Horizontal br graph
# plt.barh(x,y,height=0.3, color="green")

# plt.show()

#We can also write on top of bar graph in text format

for i, txt in enumerate(y):
    plt.text(i, txt, str(txt), va='bottom', ha='center')

plt.show()    
