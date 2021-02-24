# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10 * np.pi, 500)

y = np.sin(x)

plt.plot(x, y)
plt.show()
