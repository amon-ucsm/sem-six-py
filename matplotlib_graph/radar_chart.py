# Simple radar chart
import matplotlib.pyplot as plt
import numpy as np

lables = ['A', 'B', 'C', 'D', 'E']
data = np.array([25, 40, 20, 30, 22.5])

angles = np.linspace(0, 2 * np.pi, len(lables), endpoint= False,)
data = np.concatenate((data, [data[0]]))
angles = np.concatenate((angles, [angles[0]]))

plt.polar(angles, data, 'o-', linewidth= 2)
plt.fill(angles, data, alpha= 0.25)
plt.title('SImple Radar Chart')
plt.show()