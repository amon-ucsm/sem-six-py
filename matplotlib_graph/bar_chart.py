# Simple bar chart
import matplotlib.pyplot as plt

catergories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 20 , 30, 22.5]

plt.bar(catergories, values, color='skyblue')
plt.title('Simple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()