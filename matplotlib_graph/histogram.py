# Simple histogram
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1500)

plt.hist(data, bins= 30, color= 'skyblue', edgecolor= 'green')
plt.title('Simple Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()