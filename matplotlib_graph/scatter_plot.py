# Simple scatter plot
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = 2 * x + 1 + 0.1 * np.random.randn(100)

plt.scatter(x, y, color= 'skyblue', edgecolors= 'black')
plt.title('Simple Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()