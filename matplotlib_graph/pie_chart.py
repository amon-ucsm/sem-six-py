# Simple pie chart
import matplotlib.pyplot as plt

lables = ['A', 'B', 'C', 'D']
sizes = [25, 40, 20, 15]

plt.pie(sizes, labels= lables, autopct= '%1.1f%%')
plt.title('Simple Pie Chart')
plt.show()