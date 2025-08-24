# Simple area chart
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 15, 25, 30, 35]
y2 = [1, 6, 11, 16, 21]

plt.fill_between(x, y1, y2, color="skyblue", alpha=0.4)
plt.title('Simple Area Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()