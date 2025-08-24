# Simple line chart
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 12, 5, 8, 3]

plt.plot(x, y, marker='o', linestyle='-', color='b')
plt.title('Simple Line Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()